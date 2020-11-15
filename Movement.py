import RPi.GPIO as GPIO
import time
from MCP3008 import MCP3008

OFFSE_DUTY = 0.5        #define pulse offset of servo
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     #define pulse duty cycle for minimum angle of servo
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    #define pulse duty cycle for maximum angle of servo

servoHPin = 4
servoVPin = 15

servoHAngle = 0
servoVAngle = 0

servoHigh = 180
servoLow = 0

photoResistor1 = 0
photoResistor2 = 1
photoResistor3 = 2
photoResistor4 = 3

def map( value, fromLow, fromHigh, toLow, toHigh):  # map a value from one range to another range
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def setup():
    global servoH
    global servoV
    GPIO.setmode(GPIO.BCM)         # use PHYSICAL GPIO Numbering
    GPIO.setup(servoHPin, GPIO.OUT)   # Set servoPin to OUTPUT mode
    GPIO.output(servoHPin, GPIO.LOW)  # Make servoPin output LOW level
    GPIO.setup(servoVPin, GPIO.OUT)   # Set servoPin to OUTPUT mode
    GPIO.output(servoVPin, GPIO.LOW)  # Make servoPin output LOW level

    servoH = GPIO.PWM(servoHPin, 50)     # set Frequece to 50Hz
    servoH.start(0)                     # Set initial Duty Cycle to 0
    servoV = GPIO.PWM(servoVPin, 50)     # set Frequece to 50Hz
    servoV.start(0)                     # Set initial Duty Cycle to 0

def servoHWrite(angle):      # make the servo rotate to specific angle 
    if(angle < servoLow):
        angle = servoLow
    elif(angle > servoHigh):
        angle = servoHigh
    servoH.ChangeDutyCycle(map(angle,servoLow,servoHigh,SERVO_MIN_DUTY,SERVO_MAX_DUTY)) # map the angle to duty cycle and output it
    
def servoVWrite(angle):      # make the servo rotate to specific angle
    if(angle < servoLow):
        angle = servoLow
    elif(angle > servoHigh):
        angle = servoHigh
    servoV.ChangeDutyCycle(map(angle,servoLow,servoHigh,SERVO_MIN_DUTY,SERVO_MAX_DUTY)) # map the angle to duty cycle and output it

def loop():
    while True:
        adc = MCP3008()
        read1 = adc.read(channel = photoResistor1)
        read2 = adc.read(channel = photoResistor2)
        read3 = adc.read(channel = photoResistor3)
        read4 = adc.read(channel = photoResistor4)
        
        average12 = (read1 + read2) / 2
        average34 = (read3 + read4) / 2
        average14 = (read1 + read4) / 2
        average23 = (read2 + read3) / 2
        
        if(average12 > average34):
            servoVWrite(servoVAngle + 1)
            servoVAngle = servoVAngle + 1
            time.sleep(0.01)
        elif(average12 < average34):
            servoVWrite(servoVAngle - 1)
            servoVAngle = servoVAngle - 1
            time.sleep(0.01)
        else:
            servoVWrite(servoVAngle)
            time.sleep(0.01)
            
        if(average14 > average23):
            servoHWrite(servoHAngle + 1)
            servoHAngle = servoHAngle + 1
            time.sleep(0.01)
        elif(average14 < average23):
            servoHWrite(servoHAngle - 1)
            servoHAngle = servoHAngle - 1
            time.sleep(0.01)
        else:
            servoVWrite(servoVAngle)
            time.sleep(0.01)
            
        time.sleep(0.05)
    
def destroy():
    servoH.stop()
    servoV.stop()
    GPIO.cleanup()
    
if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
