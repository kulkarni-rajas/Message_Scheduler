import subprocess
"""
It is used to run new applications or programs through Python code by creating new processes
this is system call function of python language and it's different for different language.
"""
import sys
"""
sys module is a set of functions which provide crucial information about how your Python 
script is interacting with the host system.
"""
import schedule         # pip install schedule lets you to schedule the task
import time,datetime    # importing date time function

message = sys.argv[1]   # taking first argument from sys i.e. your terminal as message
time_format = '%H:%M'   # defining the time format
target_time = sys.argv[2]   # taking second input argument as the scheduled time
try:
    time.strptime(target_time,time_format)  # checking the given time format with time_format "H:M"
    valid_target_time = target_time         # scheduled time
except ValueError:          # if there is an error in the given time format
    valid_target_time = datetime.datetime.now() + datetime.timedelta(minutes=1)  #  timedelta gives current time plus 1 minute 
    # datetime.now() returns present time
    valid_target_time = valid_target_time.strftime(time_format)

command = "python main.py \'{}\'".format(message)   # message is formatted and sent to main.py

counter = int(str(input("Enter the number of times you want to send the message: ")).strip())
# taking input for the number of messages to be send

def job():          # function to call the main.py file at scheduled time
    for message in range(counter):
        subprocess.call(command, shell=True)    #executes the 'command' string as a valid system call in the 
                                                #terminal/command prompt
    sys.exit()      # terminate the program after sending the message

schedule.every().day.at(valid_target_time).do(job).tag('scheduling') #this line adds the job to the schedule stack 
                                                                     #inside with a given tag
# imported schedule library is used to call the function at required time

while True:  
    schedule.run_pending()      # run_pending() executes until valid target time is reached
    time.sleep(1)               # sleep or continue to run till the scheduled time is reached
