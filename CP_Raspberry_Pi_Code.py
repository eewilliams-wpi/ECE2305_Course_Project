import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BOARD)

#Calculates how how long it takes for the capacitor to charge
def rc_time(circuitPin):
    count = 0;

    #Output on the pin for
    GPIO.setup(circuitPin, GPIO.OUT)
    GPIO.output(circuitPin, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(circuitPin, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(circuitPin) == GPIO.LOW):
        count += 1

    return count;

# Threshold: there will be a threshold to determine whether or not the resistance of the photoresistor
# is high or low enough for it be considered light or dark.
def isLight(count, threshold): 
    if(count < threshold): 
        return True
        print('isLight = True')
    else:
        return False
        print('isLight = False')

if __name__=='__main__':
    count = rc_time(circuitPin)
    isLight(count, threshold)
