# Import necessary mysql libraries
import mysql.connector as mysql
import os
from dotenv import load_dotenv

# Import necessary sensor libraries
import RPi.GPIO as GPIO
import time
import hardware.button as button
import hardware.sonar as sonar

# Adjust to set sample size, runtime = samples * 1 second
samples = 20

# Loads all details from the "credentials.env"
load_dotenv('credentials.env')

# Environment Variables
db_host = os.environ['MYSQL_HOST']
db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']

# MySQL cursor
db = mysql.connect(user=db_user, password=db_pass, host=db_host)
cursor = db.cursor()

# Initialize database
def mysql_new():
    # Create a new database and select it as our current database
    cursor.execute("CREATE DATABASE IF NOT EXISTS ECE140a_Midterm;")
    cursor.execute("USE ECE140a_Midterm")

    # Deletes Sensor_Data table for running/testing code
    cursor.execute("DROP TABLE IF EXISTS Sensor_Data;")

    # Create table
    cursor.execute("""
        CREATE TABLE Sensor_Data (
        ID integer AUTO_INCREMENT PRIMARY KEY,
        distance_cm INTEGER NOT NULL,
        button_state BOOLEAN NOT NULL,    
        entered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

# Global setup, initializes database and GPIO modes for sensors
def setup():
    mysql_new()
    GPIO.setwarnings(False)
    button.setup() 
    sonar.setup()

# Gather n-many samples to insert into table
def loop():
    for i in range(samples):
        # Get real time sensor data
        distance = str(sonar.getSonar())
        button_state = str(button.detect())

        # Insert real time sonar and button data
        query = "INSERT INTO Sensor_Data (distance_cm, button_state) VALUES (%s, %s)"
        values= [(distance, button_state)]
        cursor.executemany(query, values)
        db.commit()

        print("Button state:" + button_state + "    Distance: " + distance + "cm")

        time.sleep(1)
       
if __name__ == '__main__':     
    # Program entrance
    print ("Program is starting...")
    setup()

    # Gather n-many samples then end program
    try:
        loop()
        print ("Data obtained!")
    except KeyboardInterrupt:  # Press CTRL-C to end the program
        GPIO.cleanup()         # release GPIO resources
