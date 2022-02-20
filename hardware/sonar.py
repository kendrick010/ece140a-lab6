import RPi.GPIO as GPIO
import time

trigPin = 23
echoPin = 24
MAX_DISTANCE = 220          # Define maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE*60   # Calculate timeout w.r.t to maximum distance

# Set trigPin to OUTPUT mode, echoPin to INPUT mode
def setup():
    GPIO.setmode(GPIO.BCM)     
    GPIO.setup(trigPin, GPIO.OUT)  
    GPIO.setup(echoPin, GPIO.IN)   

# Obtain pulse time of a pin under timeOut
def pulseIn(pin,level,timeOut): 
    t0 = time.time()
    while(GPIO.input(pin) != level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0
    t0 = time.time()
    while(GPIO.input(pin) == level):
        if((time.time() - t0) > timeOut*0.000001):
            return 0
    pulseTime = (time.time() - t0)*1000000
    return pulseTime

# Get measurement of ultrasonic module, unit: cm 
def getSonar():           
    GPIO.output(trigPin, GPIO.HIGH)                 # Make trigPin output 10us HIGH level
    time.sleep(0.00001)                             # 10us
    GPIO.output(trigPin,GPIO.LOW)                   # Make trigPin output LOW level
    pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   # Read echoPin pulse time
    distance = pingTime*340.0/2.0/10000.0           # Distance w/sound speed @ 340m/s
    return int(distance)

# Loops getSonar()
def loop():
    while(True):
        print("The distance is: " + str(getSonar()) + "cm")
        time.sleep(1)

# Program entrance       
if __name__ == '__main__':    
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press CTRL-C to end the program
        GPIO.cleanup()         # Release GPIO resources
