# Alex Hernandez Perez (A16543960) <br /> Kendrick Nguyen (A16045878)

> We worked on this lab on another private repository, [GitHub](https://github.com/kendrick010/ece140a-lab6), which is why we have one commit on this current repository.

## Lab 6 Objective:
The objective of this lab is incorporate web development skills we have learned from the previous labs with hardware, specificaly with the Raspberry Pi.

## a. Tutorial 1 Setup Raspberry Pi: 
In this tutorial, we learned how to setup a raspberry pi, enabling SSSH and mysql access. Once configured, we were able to run the same code from the previous labs but on the raspberry pi.

## b. Tutorial 2 Basic I/O:
In this tutorial, we learned how to use the i/o pins on the raspberry pi with the ultrasonic sensor and piezo buzzer. From the tutorial, we obtained printed distance data obtained from the ultrasonic sensor.

## c. Challege 1 Midterm: 
> [YouTube](https://youtu.be/4FGcyNgpSbQ) submission link

The project we created is the Sonic Reader Button. It is essentially a webserver application that collects periodic sensor readings from an ultrasonic sensor and a button. The collected data is stored into a MySQL database for it be conveniently accessed by the webserver to fetch, query, and display data on the webage.

1. [To get started, build the following schematic.](/hardware/circuit)

    ![Alt text](/hardware/circuit/schematicA.png)

2. Run the server
    ```
    python app.py
    ```

3. Proceed to your browser to `http://localhost:6543`. The page should render like so. 
    ![Alt text](/doc/images/webpage.png)

4. Collect some data! Start by pressing the `Record` button and place your in front of the ultrasonic sensor. A good indication that the program is currently recording data is if the LED is ON.

    Vary your hand distance to obtain a range of distances. Simultaneously, you can also press the button. By default, the sample size is 20, and we record one sample a second. However, you can modify the number of samples in the `init-db.py` file.

    You may stop inputting data once the LED toggles OFF. The webpage will also present a message notifying when data collection has finished.

5. You can view a table of the data you produced by clicking the `Display` button.
    ![Alt text](/doc/images/webpage_table.png)

6. Explore by clicking the `Submit` buttons on the right. 
    
    On the distance criteria, clicking the `Submit` will output the first instance of your selected distance range in your produced data..

    On the button criteria, clicking the `Submit` will output the first instance of your selected button state in your produced data.

    On the both criteria, clicking the `Submit` will output the first instance satisfying both the selected distance range and button state in your produced data.

> Note: Attempting to click any of the buttons on the webpage while in the middle of recording data will not affect anything. The program runs sequentially.

## c. Challege 1 Midterm Code:
> [README.md](/doc/README.md) code explanations

    - /hardware
        - button.py
        - LED.py
        - sonar.py
    - /public
        - rest.js
        - simple.css
    - app.py
    - credentials.env
    - index.html
    - init_db.py
