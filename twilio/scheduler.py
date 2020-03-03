import subprocess
"""
The subprocess module present in Python(both 2.x and 3.x) 
is used to run new applications or programs through Python code by creating new processes.
this is system call function of python language and it's different for different language.
"""
import sys

"""

"""

message = sys.argv[1]

check="echo \'{}\'".format(message)
subprocess.call(check,shell=True)

try:
    time = sys.argv[2]
except IndexError:
    time = "now"
command = 'echo "export DISPLAY=:0 && python main.py \'{}\'" | at {}'.format(message, time)

subprocess.call(command, shell=True)
