# pip install schedule
import schedule # necessary for scheduling 
# documentation: https://schedule.readthedocs.io/en/stable/api.html
import time
from MCP3008 import MCP3008
from Movement import *
from multiprocessing import *

def adjust_servo():
    print("Servo Angle Adjustment...")

def read_photoresistor():
    adc = MCP3008()
    read1 = adc.read1(channel = 0) #channel 0
    read2 = adc.read2(channel = 1) #channel 1
    read3 = adc.read3(channel = 2) #channel 2
    read4 = adc.read4(channel = 3) #channel 3

    return [read1, read2, read3, read4]

def move_panel(): 
    setup()
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
        
    if(average14 > average23):
        if(servoHAngle < servoHigh):
            servoHWrite(servoHAngle + 1)
            servoHAngle = servoHAngle + 1
        else:
            servoHAngle = servoHigh
        time.sleep(0.01)
    elif(average14 < average23):
        if(servoHAngle > servoLow):
            servoHWrite(servoHAngle - 1)
            servoHAngle = servoHAngle - 1
        else:
            servoHAngle = servoLow
        time.sleep(0.01)
    else:
        servoVWrite(servoVAngle)
        time.sleep(0.01)
    
    #print('ServoH: ', servoHAngle)
    print('ServoV: ', servoVAngle)



# scheduling templates for later
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

def run_sheduled_jobs():
    while True:
        schedule.run_pending() # runs the jobs that are scheduled, does not run missed tasks 
        time.sleep(1)

def movement_schedule():
    schedule.every(10).seconds.do(move_panel)
    run_sheduled_jobs()

def run_jobs():
    movement_proc = Process(target = movement_schedule)
    movement_proc.start()
    movement_proc.join()

# developer notes: 
# need to make sure script can run in parallel 
# test for which time zone is scheduled (also consider Daylight Saving)