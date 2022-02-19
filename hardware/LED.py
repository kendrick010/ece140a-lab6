import RPi.GPIO as GPIO
import time
   
def setup():
    ledPin = 25
    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(ledPin, GPIO.OUT)    # set ledPin to OUTPUT mode

def toggle():
    ledPin = 25
    GPIO.output(ledPin, not(GPIO.input(ledPin)))

def loop():
    while(True):
        toggle()
        time.sleep(1)

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press CTRL-C to end the program
        GPIO.cleanup()         # release GPIO resources
