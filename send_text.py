#from twilio.rest import Client
from twilio  import rest
# Your Account SID from twilio.com/console
account_sid = "ACefaea53f99cfbaf86d7ddea0c5e010e1"
# Your Auth Token from twilio.com/console
auth_token  = "939bf49af0dc386e126b43b54a6f978b"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+919561412760", 
    from_="+19252939155",
    body="Hello from Python!")

print(message.sid)
