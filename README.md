# Message_Scheduler
A python script to send messages.

##  Requirements for twilio
+ Python
+ Python-pip
+ twilio

## Setup
1. Clone the app ``` git clone https://github.com/rohitsh16/Message_Scheduler.git ```
2. ```mkdir project && cd project```
3. ```pip install twilio```
4. ```Create a free account on twilio```
5. ```Create a twilio number and put twilio number and account ssid also auth token```
6. ```Add a verified caller ID by adding number in which you want to send message```

## Usage
### Simple Twilio Message
``` python main.py "message" ```

### Twilio scheduled Message
``` python schedule.py "message" HH:MM ```
