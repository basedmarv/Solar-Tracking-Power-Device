# pip install schedule
# import schedule # necessary for scheduling 
# documentation: https://schedule.readthedocs.io/en/stable/api.html
import time, traceback #, datetime
from MCP3008 import MCP3008
# from Movement import *
# from multiprocessing import *
import RPi.GPIO as GPIO
import threading
import signal
from dbms_connection import *
from voltage import *

OFFSE_DUTY = 0.5        #define pulse offset of servo
SERVO_MIN_DUTY = 2.5+OFFSE_DUTY     #define pulse duty cycle for minimum angle of servo
SERVO_MAX_DUTY = 12.5+OFFSE_DUTY    #define pulse duty cycle for maximum angle of servo

adc = MCP3008()

servoHPin = 17  #GPIO17 
servoVPin = 21   #GPI21

servoHAngle = 90
servoVAngle = 90
servoHigh = 100 #50 is the adjusted angle
servoLow = 0
photoResistor1 = 0 #top left
photoResistor2 = 1 #top right
photoResistor3 = 2 #bottom right
photoResistor4 = 3 #bottom left 

AO_pin = 4 #channel pin 4
A1_pin = 5 #channel pin 4
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

def map( value, fromLow, fromHigh, toLow, toHigh):  # map a value from one range to another range
    return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow

def setup():
    global servoH
    global servoV
    #global servoHigh 
    #global servoLow
    GPIO.setmode(GPIO.BCM)         # use PHYSICAL GPIO Numbering
    GPIO.setup(servoHPin, GPIO.OUT)   # Set servoPin to OUTPUT mode
    GPIO.output(servoHPin, GPIO.LOW)  # Make servoPin output LOW level
    GPIO.setup(servoVPin, GPIO.OUT)   # Set servoPin to OUTPUT mode
    GPIO.output(servoVPin, GPIO.LOW)  # Make servoPin output LOW level

    servoH = GPIO.PWM(servoHPin, 50)     # set Frequece to 50Hz
    servoH.start(0)                     # Set initial Duty Cycle to 0
    servoV = GPIO.PWM(servoVPin, 50)     # set Frequece to 50Hz
    servoV.start(0)                     # Set initial Duty Cycle to 0
    
    #GPIO.setup(SPIMOSI, GPIO.OUT) 
    #GPIO.setup(SPIMISO, GPIO.IN)
    #GPIO.setup(SPICLK, GPIO.OUT)
    #GPIO.setup(SPICS, GPIO.OUT)
    pass

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

def read_photoresistor():
    global adc
    read1 = adc.read1(channel = 0) #channel 0
    read2 = adc.read2(channel = 1) #channel 1
    read3 = adc.read3(channel = 2) #channel 2
    read4 = adc.read4(channel = 3) #channel 3

    return [read1, read2, read3, read4]

def move_panel(): 
    global servoHAngle 
    global servoVAngle 
    global photoResistor1 
    global photoResistor2 
    global photoResistor3 
    global photoResistor4 
    global servoHigh 
    global servoLow

    #while True:
    t_end = time.time() + 10
    print("Tracking in progress....")
    while time.time() < t_end: 
        adc_readings = read_photoresistor()

        average12 = (adc_readings[0] + adc_readings[1]) / 2
        average34 = (adc_readings[2] + adc_readings[3]) / 2
        average14 = (adc_readings[0] + adc_readings[3]) / 2
        average23 = (adc_readings[1] + adc_readings[2]) / 2

        
        if(average12 < average34):
            if(servoVAngle < servoHigh):
                servoVWrite(servoVAngle + 1)
                servoVAngle = servoVAngle + 1
            else:               
                servoVAngle = servoHigh
            time.sleep(0.01)
        elif(average12 > average34):
            if(servoVAngle > servoLow):
                servoVWrite(servoVAngle - 1)
                servoVAngle = servoVAngle - 1
            else:
                servoVAngle = servoLow
            time.sleep(0.01)
        else:
            servoVWrite(servoVAngle)
            time.sleep(0.01)
            
        if(average14 < average23):
            if(servoHAngle < servoHigh):
                servoHWrite(servoHAngle + 1)
                servoHAngle = servoHAngle + 1
            else:
                servoHAngle = servoHigh
            time.sleep(0.01)
        elif(average14 > average23):
            if(servoHAngle > servoLow):
                servoHWrite(servoHAngle - 1)
                servoHAngle = servoHAngle - 1
            else:
                servoHAngle = servoLow
            time.sleep(0.01)
        else:
            servoHWrite(servoHAngle)
            time.sleep(0.01)

        #if (time.time() == t_end - 1):
    print(f'Tracking finished.\nNew servoVAngle: {servoVAngle}')
    print(f'Tracking finished.\nNew servoHAngle: {servoHAngle}')
            #voltage_val = readadc(0, 11, 9, 10, 8)
            #ad_value = readadc(AO_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
            #solarVoltage= ad_value*(3.3/1024)*5
            #print(f'Solar voltage: {solarVoltage}.')
            #time.sleep(1) 
            #ad_value = readadc(A1_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
            #batteryVoltage= ad_value*(3.3/1024)*5
            #print(f'Battery voltage: {batteryVoltage}.')
            #time.sleep(1)
            #insert_data(time = calculate_time(), latitude = servoVAngle, longitude = servoHAngle, voltage = solarVoltage) # need time, verify latitude and longitude, and voltage
    
def calculate_time():
    now = datetime.datetime.now()
    hour = now.hour
    
    if(now.minute > 15 and now.minute <= 30):
        minute = 0.25
    elif(now.minute > 30 and now.minute <= 45):
        minute = 0.50
    elif(now.minute > 45 and now.minute <= 60):
        minute = 0.75
    else:
        minute = 0

    return hour + minute     

def every(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task()
    except Exception:
      traceback.print_exc()
      # in production code you might want to have this instead of course:
      # logger.exception("Problem while executing repetitive task.")
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay

def destroy(signal, frame):
    servoH.stop()
    servoV.stop()
    GPIO.cleanup()
    exit(0)

def run_jobs():
    setup()
    #move_panel()
    threading.Thread(target=lambda: every(20,move_panel)).start()
    
    signal.signal(signal.SIGINT, destroy)
    #threading.Thread(target=every(1800,insert_data)).start()
    # movement_proc = Process(target = movement_schedule)
    # movement_proc.start()
    # movement_proc.join()


# scheduling templates for later
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

# def run_sheduled_jobs():
#     while True:
#         schedule.run_pending() # runs the jobs that are scheduled, does not run missed tasks 
#         time.sleep(1)

# def movement_schedule():
#     schedule.every(1).seconds.do(adjust_servo)
#     run_sheduled_jobs()

# if __name__ == '__main__':
#     setup()
#     move_panel()
