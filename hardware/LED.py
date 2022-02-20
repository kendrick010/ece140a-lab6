import RPi.GPIO as GPIO
import time

ledPin = 25

# Set ledPin to OUTPUT mode
def setup():
    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(ledPin, GPIO.OUT)

# Turns off led when on, turns on led when off
def toggle():
    GPIO.output(ledPin, not(GPIO.input(ledPin)))

# Call this to loop toggle(), essentially a blink example
def loop():
    while(True):
        toggle()
        time.sleep(1)

# Program entrance
if __name__ == '__main__':     
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press CTRL-C to end the program
        GPIO.cleanup()         # Release GPIO resources
