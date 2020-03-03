import subprocess
import sys
import schedule
import time,datetime

message = sys.argv[1]
time_format = '%H:%M'
target_time = sys.argv[2]
try:
    time.strptime(target_time,time_format)
    valid_target_time = target_time
except ValueError:
    valid_target_time = datetime.datetime.now() + datetime.timedelta(minutes=1)
    valid_target_time = valid_target_time.strftime(time_format)

command = "python main.py \'{}\'".format(message)

counter = int(str(input("Enter the number of times you want to send the message: ")).strip())

def job():
    for message in range(counter):
        subprocess.call(command, shell=True)
    sys.exit()

schedule.every().day.at(valid_target_time).do(job).tag('scheduling')

while True:  
    schedule.run_pending() 
    time.sleep(1) 
