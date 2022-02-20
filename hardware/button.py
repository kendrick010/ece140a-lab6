import RPi.GPIO as GPIO
import time

buttonPin = 26

# Set buttonPin to INPUT mode with pull-up resistor
def setup():
    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    

# If button pressed return 1, else return 0
def detect():
    return 1 if GPIO.input(buttonPin) == GPIO.LOW else 0

# Loops detect(). give one second buffer
def loop():
    while(True):
        print(detect())
        time.sleep(1)

# Program entrance       
if __name__ == '__main__':     
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press CTRL-C to end the program
        GPIO.cleanup()         # Release GPIO resources