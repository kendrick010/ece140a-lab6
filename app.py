#import all the necessary libraries
from wsgiref.simple_server import make_server
import cv2
from pyramid.config import Configurator
from pyramid.response import FileResponse

import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv('credentials.env')
 
''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']


response = {
    'error':   "no_error",
    'id':           "",
    'distance':         "",
    'button':  "",
    'timestamp':        ""
}
# function to access data
def get_data(req):
   #get the id from the request
  id = req.matchdict['id']
  id = int(id)#value was string so cast to int
  print(id)
  #print(type(id))
  #print(type(150))

  #connect to the database
  db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
  cursor = db.cursor()
  
  if id > 0 and id <= 15  : # if value passed is within bounds than we want height
     if (id==1):
         id = 0
     query = "SELECT * from test_data where distance >= {} && distance < {};".format(id, id + 5)
     cursor.execute(query)
     record = cursor.fetchone()
     print(record)     
     #print(type(record))
     db.close()
     if record is None:
      return {
      'error' : "No data was found for the given ID" ,
      'id': "",
      'distance' : "",
      'button': "",
      'timestamp': ""
    }
     response['id'] =record[0]
     response['distance'] =record[1]
     response['button'] =record[2]
     response['timestamp'] =record[3]

 

  elif id == 0 or id >= 20 and id <=40: 
     if(id == 0):
         id = id +10

     query = "SELECT * from test_data where created >= {} && created < {};".format(id - 10, id )
     cursor.execute(query)
     record = cursor.fetchone()
     print(record)     
     #print(type(record))
     db.close()
     if record is None:
      return {
      'error' : "No data was found for the given ID" ,
      'id': "",
      'distance' : "",
      'button': "",
      'timestamp': ""
    }
     response['id'] =record[0]
     response['distance'] =record[1]
     response['button'] =record[2]
     response['timestamp'] =record[3]

  return response

def get_both(req):
       #get the id from the request
  id = req.matchdict['id']
  id = int(id)#value was string so cast to int
  print(id)
  #print(type(id))
  #print(type(150))

  #connect to the database
  db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
  cursor = db.cursor()
  
  str_id = str(id) #convert back to string for slicing
  if(len(str_id) == 3):
      if(str_id[2] ==0):
          distance = str_id[0:2]
          age = str_id[2]
          age = int(age)+10
          age = str(age)
      else:
          distance = str_id[0]
          age = str_id[1:]
  elif(len(str_id)== 2):
      if(str_id[0] == 1):
          distance = 0
          age = str_id[1]
          age = int(age)+10
          age = str(age)
      else:
          distance = str_id[0]
          age = str_id[1]
          age = int(age)+10
          age = str(age)
  else:
      distance = str_id[0:2]
      age = str_id[2:]
  print(age)
  print(distance)
  age = int(age)#convert back to ints 
  distance = int(distance)# so we can add upper bound 
   #execute query like normal
  query = "SELECT * from test_data WHERE distance >= {} && distance < {} && created >= {} && created < {};".format(distance, distance + 5, age-10, age)
  cursor.execute(query)
  record = cursor.fetchone()
  print(record) 
  db.close()
  if record is None:
      return {
          'error' : "No data was found for the given ID" ,
          'id': "",
          'distance' : "",
          'button': "",
          'timestamp': ""
          }
  response['id'] =record[0]
  response['distance'] =record[1]
  response['button'] =record[2]
  response['timestamp'] =record[3]
  return response



def index_page(req):
   return FileResponse("index.html")



if __name__ == '__main__':
   with Configurator() as config:
       # Create a route called home
       config.add_route('home', '/')
       # Bind the view (defined by index_page) to the route named ‘home’
       config.add_view(index_page, route_name='home')
      
       # Create a route that handles server HTTP requests at: /photos/photo_id
       config.add_route('data', '/data/{id}')
       
       config.add_route('both','both/{id}')

       # Binds the function get_photo to the photos route and returns JSON
       # Note: This is a REST route because we are returning a RESOURCE!
       config.add_view(get_data, route_name='data', renderer='json')

       config.add_view(get_both, route_name='both', renderer='json')
 
       # Add a static view
       # This command maps the folder “./public” to the URL “/”
       # So when a user requests geisel-1.jpg as img_src, the server knows to look
       # for it in: “public/geisel-1.jpg”
       config.add_static_view(name='/', path='./public', cache_max_age=3600)
      
       # Create an app with the configuration specified above
       app = config.make_wsgi_app()
   # start the server on port 6543
   server = make_server('0.0.0.0', 6543, app) 
   server.serve_forever()