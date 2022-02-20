# Import all server libraries
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse
from pyramid.renderers import render_to_response

# Import all mysql libraries
from datetime import datetime, date, timedelta
import mysql.connector as mysql
from dotenv import load_dotenv
import os

# Import all hardware libraries
import RPi.GPIO as GPIO
import hardware.LED as led 
import init_db as sense

# Loads all details from the 'credentials.env'
load_dotenv('credentials.env')
 
# Environment variables
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# JSON response
response = {
    'error':        "no_error",
    'id':           "",
    'distance':     "",
    'button':       "",
    'timestamp':    ""
}

# JSON reponse error
response_none = {
    'error' :       "No data was found" ,
    'id':           "",
    'distance' :    "",
    'button':       "",
    'timestamp':    ""
}

# Return html webpage for home route
def index_page(req):
    return FileResponse("index.html")

# Record sensor data, if successful, returns msg key
def record(req):
    # Configure LED
    led.setup()
    led.toggle()

    # Configure button and sonar
    sense.setup()
    sense.loop()

    # Turns off led once data finished recording
    led.toggle()

    return {'msg': 'New data has been collected'}

# Collection route, get all data to render table
def get_all(req):

    # Connect to database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()
    cursor.execute("select * from Sensor_Data;")
    records = cursor.fetchall()
    db.close()

    # Format the result as key-value pairs
    response = {}
    for index, row in enumerate(records):
        response[index] = {
            "id":           row[0],
            "distance":     row[1],
            "button":       row[2],
            "timestamp":    str(row[3])
        }

    # Return json data to html page
    data = {"responses": records}
    return render_to_response('index.html', data, request=req)

# Function to access distance data
def get_distance(req):
    # Get distance range from request
    distance_range = req.matchdict['distance']
    distance_range = distance_range.split('-')

    # Get min and max distance value
    distance_min = distance_range[0]
    distance_max = distance_range[1]

    # Connect to database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # Query for button criteria
    cursor.execute("select * from Sensor_Data where distance_cm between " + str(distance_min) + " and " + str(distance_max) + ";")
    record = cursor.fetchone()
    db.close()

    if record is None:
        return response_none

    # Return queried json data
    response['id'] = record[0]
    response['distance'] = record[1]
    response['button'] = record[2]
    response['timestamp'] = str(record[3])

    return response

# Function to access distance data
def get_button(req):
    # Get button state from request
    button_state = req.matchdict['button']

    # Connect to database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # Query for button criteria
    cursor.execute("select * from Sensor_Data where button_state = " + str(button_state) + ";")
    record = cursor.fetchone()
    db.close()

    if record is None:
        return response_none

    # Return queried json data
    response['id'] = record[0]
    response['distance'] = record[1]
    response['button'] = record[2]
    response['timestamp'] = str(record[3])

    return response

# Function to access both distance and button data
def get_both(req):
    # Get distance from request
    distance_range = req.matchdict['distance']
    distance_range = distance_range.split('-')

    # Get min and max distance value
    distance_min = distance_range[0]
    distance_max = distance_range[1]

    # Get button state from request
    button_state = req.matchdict['button']

    # Connect to database
    db = mysql.connect(host=db_host, user=db_user, passwd=db_pass, database=db_name)
    cursor = db.cursor()

    # Query for both distance and button criteria
    query = "select * from Sensor_Data where distance_cm between " + str(distance_min) + " and " + str(distance_max) + " and button_state = " + str(button_state) + ";"
    cursor.execute(query)
    record = cursor.fetchone()
    db.close()

    if record is None:
        return response_none

    # Return queried json data
    response['id'] = record[0]
    response['distance'] = record[1]
    response['button'] = record[2]
    response['timestamp'] = str(record[3])

    return response

if __name__ == '__main__':
    try:
        with Configurator() as config:

            # Use Jinja2 to render Sensor_Data table
            config.include('pyramid_jinja2')
            config.add_jinja2_renderer('.html')

            # Create a route called home, bind the view (defined by index_page) to the route named ‘home’
            config.add_route('home', '/')
            config.add_view(index_page, route_name='home')

            # Create a route called record, binds the function record to the /record route and returns JSON
            config.add_route('record', '/record')
            config.add_view(record, route_name='record', renderer='json')

            # Create a route called getall, binds the function get_all to the /getall route and returns JSON
            config.add_route('getall', '/getall')
            config.add_view(get_all, route_name='getall')

            # Create a route called distance, binds the function get_distance to the /distance/{id} route and returns JSON
            config.add_route('distance', '/distance/{distance}')
            config.add_view(get_distance, route_name='distance', renderer='json')

            # Create a route called button, binds the function get_button to the /button/{id} route and returns JSON
            config.add_route('button', '/button/{button}')
            config.add_view(get_button, route_name='button', renderer='json')
        
            # Create a route called both, binds the function get_both to the /both/{distance}/{button} route and returns JSON
            config.add_route('both','both/{distance}/{button}')
            config.add_view(get_both, route_name='both', renderer='json')
    
            # Add a static view
            config.add_static_view(name='/', path='./public', cache_max_age=3600)
        
            # Create an app with the configuration specified above
            app = config.make_wsgi_app()

        # Start the server on port 6543
        server = make_server('0.0.0.0', 6543, app) 
        server.serve_forever()   
    
    except KeyboardInterrupt:  # Press CTRL-C to end the program
        GPIO.cleanup()         # Release GPIO resources