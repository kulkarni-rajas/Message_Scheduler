
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import sys 

account_sid = 'AC36b3fd3b15e6e12cf39260e7dfca2ac7'
auth_token = 'd36bc92ecd1c144c6b40a92214bf9c20'
client = Client(account_sid, auth_token)
message = sys.argv[1]
for i in range(0,1):
     try:
          message_create = client.messages.create(
                    #  body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     body=message,
                     from_='+19789652505',
                     to='+919875391518'
               )

          print(message_create.sid)
     except:
          print("Invalid Number")