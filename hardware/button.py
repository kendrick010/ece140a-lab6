import RPi.GPIO as GPIO
import time

buttonPin = 25
   
def setup():
    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to INPUT mode with pull-up resistor

def detect():
    # if button pressed return 1, else return 0
    return 1 if GPIO.input(buttonPin) == GPIO.LOW else 0

def loop():
    while(True):
        print(detect())
        time.sleep(1)
       
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press CTRL-C to end the program
        GPIO.cleanup()         # release GPIO resources