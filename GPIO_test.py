##File used for GPIO pin configuration testing##

import RPi.GPIO as GPIO
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
print("LED ON")
GPIO.output(4,GPIO.HIGH)
time.sleep(5)
print("LED OFF")
GPIO.output(4,GPIO.LOW)
