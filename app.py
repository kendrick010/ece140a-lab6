#import all the necessary libraries
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse
from pyramid.renderers import render_to_response
from datetime import datetime,date

import mysql.connector as mysql
from dotenv import load_dotenv
import os

import test as led 


load_dotenv('credentials.env')
 
''' Environment Variables '''
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


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
     query = "SELECT * from Sensor_Data where distance_cm between {} and {};".format(id, id + 5)
     cursor.execute(query)
     record = cursor.fetchone()
    #  print(record)     
     for r in record:
        print(r)
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
     response['timestamp'] =str(record[3])

  elif id == 0 or id == 30: 

     query_time =  str(today) +" "+ current_time
     query_time_L = query_time[0:17] + str(id)
     query_time_h = query_time[0:17] + str(id + 30)
    #  print(query_time_L)
    #  print(query_time_h)
     query = "SELECT * from Sensor_Data where entered_at between '"+query_time_L+"' and '"+query_time_h+"'"
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
     response['timestamp'] = str(record[3])

  return response

def get_both(req):
       #get the id from the request
  id = req.matchdict['id']
  id = int(id)#value was string so cast to int
  print(id)

  #connect to the database
  db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
  cursor = db.cursor()
  
  str_id = str(id) #convert back to string for slicing
  if(len(str_id) == 3):
      if(str_id[2] == '0'):#case where ID 3 digtis and last one is 0 means age os 0-30
          distance = str_id[0:2]#meaning first distance is 2 dig number
          age = str_id[2]
          age = int(age)
      elif(str_id[1:] == '30'):#else then we have age of 30-60
          distance = str_id[0]#and distance is single digit
          age = str(str_id[1:])
  elif(len(str_id)== 2):
      if(str_id[0] == '1'):#case where ID is 10 indicating a distance of 0-10 and age of 0-30
          distance = 0
          age = str_id[1]
          age = int(age)
      else:#case 5 0 
          distance = str_id[0]
          age = str_id[1]
          age = int(age)
  else:#other wise 4 digit ID 
      distance = str_id[0:2]
      age = str_id[2:]
  print(age)
  print(distance)
  age = int(age)#convert back to ints 
  distance = int(distance)
   #execute query like normal
  query_time =  str(today) +" "+ current_time
  query_time_L = query_time[0:17] + str(age)
  query_time_h = query_time[0:17] + str(age + 30)
  print(query_time_L)
  print(query_time_h)
  query = "select * from sensor_data where entered_at between '{}' and '{}' and distance_cm between {} and {};".format(query_time_L,query_time_h,distance,distance +10)
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
  response['timestamp'] = str(record[3])
  return response



def get_all(req):
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()
    cursor.execute("select * from Sensor_Data;")
    records = cursor.fetchall()
    db.close()
  # Format the result as key-value pairs
    response = {}
    for index, row in enumerate(records):
        response[index] = {
        "id": row[0],
        "distance": row[1],
        "button": row[2],
        "timestamp": str(row[3])
    }
    data = {"responses": records}
    return render_to_response('index.html', data, request=req)

def index_page(req):
    
   return FileResponse("index.html")

def do_led(req):
    led.setup()
    print("helloworld")
    led.toggle()
    return None


if __name__ == '__main__':

    
   with Configurator() as config:
       # Create a route called home
       config.add_route('home', '/')
       # Bind the view (defined by index_page) to the route named ‘home’
       config.add_view(index_page, route_name='home')
       config.include('pyramid_jinja2')
       config.add_jinja2_renderer('.html')


       config.add_route('data', '/data/{id}')
       
       config.add_route('both','both/{id}')

       config.add_route('led', '/led')
       
       config.add_route('getall', '/getall')


       # Binds the function get_photo to the photos route and returns JSON
       # Note: This is a REST route because we are returning a RESOURCE!
       config.add_view(get_data, route_name='data', renderer='json')

       config.add_view(get_both, route_name='both', renderer='json')

       config.add_view(do_led,route_name='led')

       
       config.add_view(get_all,route_name='getall')
 
       # Add a static view
       # This command maps the folder “./public” to the URL “/”
       # So when a user requests geisel-1.jpg as img_src, the server knows to look
       config.add_static_view(name='/', path='./public', cache_max_age=3600)
      
       # Create an app with the configuration specified above
       app = config.make_wsgi_app()
   # start the server on port 6543
   server = make_server('0.0.0.0', 6543, app) 
   server.serve_forever()