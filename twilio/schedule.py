import subprocess
import sys

message = sys.argv[1]
check="echo \'{}\'".format(message)
subprocess.call(check,shell=True)
try:
    time = sys.argv[2]
except IndexError:
    time = "now"
command = 'echo "export DISPLAY=:0 && python p4.py \'{}\'" | at {}'.format(message, time)
subprocess.call(command, shell=True)