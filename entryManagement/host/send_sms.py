# File handles sending sms
# Please update your credentials in settings.py before running

# WARNING:
# Update ACCOUNT_SID with your twilio account_sid in line 136 in setting.py
# Update AUTH_TOKEN with your twilio auth_token in line 137 in setting.py

from twilio.rest import Client
from django.conf import settings


def sendSms(msg, receiver):
    account_sid = settings.ACCOUNT_SID
    auth_token = settings.AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=msg,
        from_='+12053950162',
        to='+91' + str(receiver)
    )
