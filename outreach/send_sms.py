from twilio.rest import Client

account_sid = 'AC749e2abbc49ba'
auth_token = '2f2df404bd5ed7'
client = Client(account_sid, auth_token)

def send_sms(to, body):
    message = client.messages.create(
        to=to,
        from_='+16187042',
        body=body
    )
    return message.sid
