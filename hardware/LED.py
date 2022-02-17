import RPi.GPIO as GPIO
import time

ledPin = 25
   
def setup():
    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(ledPin, GPIO.OUT)    # set ledPin to OUTPUT mode

def loop():
    while(True):
        GPIO.output(ledPin, not(GPIO.input(ledPin)))
        time.sleep(1)

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press CTRL-C to end the program
        GPIO.cleanup()         # release GPIO resources
