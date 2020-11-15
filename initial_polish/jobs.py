# pip install schedule
import schedule # necessary for scheduling 
# documentation: https://schedule.readthedocs.io/en/stable/api.html
import time

def adjust_servo():
    print("Servo Angle Adjustment...")


# scheduling templates for later
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

schedule.every(10).seconds.do(adjust_servo)


while True:
    schedule.run_pending() # runs the jobs that are scheduled, does not run missed tasks 
    time.sleep(1)

# developer notes: 
# need to make sure script can run in parallel 
# test for which time zone is scheduled (also consider Daylight Saving)