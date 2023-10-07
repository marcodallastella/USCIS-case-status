import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(from_email='md3934@columbia.edu',
                to_emails='dallastella.marco@gmail.com',
                subject='Sending with Twilio Sendgrid is Fun' ,
                plain_text_content='and esay to do anywhere, even with Python.',
                html_content='<strong>and easy to do anywhere, even with Python</strong')

try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print(e.message)