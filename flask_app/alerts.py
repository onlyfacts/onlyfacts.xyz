import smtplib
import json
from email.message import EmailMessage


with open('../config.json', 'r') as f:
    conf = json.load(f)

EMAIL_ADDRESS = conf['EMAIL_SEND']
EMAIL_PASSWORD = conf['EMAIL_SEND_PASS']
contacts = conf['EMAILS_RECEIVE']

def send(subject, message):
    """ Sends email to my phone number. """
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts
    msg.set_content(
        '\n'.join([f'{key}: {value}\n' for key, value in message.items()])
    )
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
