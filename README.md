# Message_Scheduler
A python script to send messages.

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
<br>

##  Requirements for twilio
+ Python
+ Python-pip
+ twilio
+ schedule

## Setup
1. Clone the app ``` git clone https://github.com/rohitsh16/Message_Scheduler.git ```
2. ```cd Message_Scheduler```
3. ```pip install -r requirements.txt```
4. ```cd twilio```
5. ```Create a free account on twilio```
6. ```Get a twilio number.```
7. ```Put account ssid and auth token in the python script.```
8. ```Add a verified caller ID by adding and verifying number in twilio in which you want to send message```

## Usage
```Inside the twilio directory```

### Simple Twilio Message
``` python main.py "{{ your_message }}" ```

### Twilio scheduled Message
``` python automate.py "{{ your_message }}" "HH:MM" ```
