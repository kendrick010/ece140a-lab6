
import RPi.GPIO as GPIO
import time

ledPin = 25
   
def setup():
    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(25, GPIO.OUT)    # set ledPin to OUTPUT mode

def toggle():
    GPIO.output(25, not(GPIO.input(25)))

def loop():
    while(True):
        toggle()
        time.sleep(1)
