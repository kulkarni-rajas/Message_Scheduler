import plivo
import sys

account_id = "your_auth_id_here"
account_token = "your_auth_token_here"
client = plivo.RestClient(auth_id=account_id , auth_token=account_token)
info = sys.argv[1]
for i in range(0,1):
    try:
        message_created = client.messages.create(
            src='source_number_here',
            dst='destination_number_here',
            text=info
        )
    except:
        print("Invalid number")