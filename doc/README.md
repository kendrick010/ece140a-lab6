# Challege 1 Midterm Code:

## a. `button.py`:
Simple button circuit and code, detects when the user has pressed the button or not. Calling `detect()` will return the button state.

To test, run

```
python button.py
```

## b. `LED.py`:
Simple LED circuit and code, toggles LED ON when initially OFF (and vice versa). Calling `toggle()` will toggle the LED ON/OFF depending on the current state of the LED.

To test, run

```
python LED.py
```

## c. `sonar.py`:
Simple ultrasonic sensor circuit and code, detects and reads distance from an nearby object. Calling `sonar()` will measure the distance from the nearby object and returns integer distance reading in centimeters.

To test, run

```
python sonar.py
```

## d. `rest.js`
Handles all event functions, whenever a user requests a server route or clicks a button, within the webpage. For the case of buttons, a route request occurs and the program converts the response to a JSON pertaining to a query. Webpage updates the inner HTML relating to contents of the response JSON.

## e. `simple.css`
Briefly, a styling sheet for the `index.html` webpage. Organizes all data collecting features on the left and all querying features on the right.

## f `app.py`
Starts RESTful server, creating and adding routes for all requests in `rest.js`. Additionally, `record()` will call the functions from `init-db.py` and `led.py` to start recording/logging sensor data and indicate when the recording has finished.

To test, run
```
python app.py
```

## g. `credentials.env`
Configuration file containing all MySQL environment variables, such as host address, username, password, and used database

## h. `index.html`
Server webpage HTML document. Will render once the user accesses `http://localhost:6543` or `http://localhost:6543/getall`

## i `init_db.py
Initializes a database, `ECE140a_Midterm` and database table, `Sensor_Data`, to store button and sonar data.

Calls `button.py` and `sonar.py` to record data and insert into database table, `Sensor_Data`. You can vary the sample size (as 20 is the default size), but program records and inserts sensor data every one second.

To test, run

```
python init_db.py
```