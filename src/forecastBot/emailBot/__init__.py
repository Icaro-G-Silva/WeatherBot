import os
import json
import smtplib
from email.message import EmailMessage
from datetime import datetime
from forecastBot import validations

valid = validations.EmailValidation()
path = os.path.join(os.path.dirname(__file__), '../../archive/config.json')

class MailBot:
    def __init__(self, mailTo = False, subject = False, message = False):
        valid.validateInput(mailTo, subject, message)
        self.mail = EmailMessage()
        self.mail['Subject'] = subject
        self.mail['To'] = mailTo
        self.mail.set_content(message)
        
    def send(self):
        print('Sendind the email...')
        with open(path, 'r') as config:
            configObject = json.loads(config.read())
        self.mail['From'] = configObject['smtpUser']
        with smtplib.SMTP_SSL(configObject['smtpServer'], configObject['smtpPort']) as smtp:
            smtp.login(configObject['smtpUser'], configObject['smtpPassword'])
            smtp.send_message(self.mail)
        print('Email sent')
