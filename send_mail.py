import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv('.secure')

smtp_server = 'smtp.gmail.com'
smtp_port = 465
sender_email = os.getenv('sender_email')
app_password = os.getenv('app_password')
receiver_email = os.getenv('receiver_email')
subject = 'Site position report'
body = 'Report is attached to the mail body'

file_path = 'position_report.xlsx'

msg = EmailMessage()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.set_content(body)

with open(file_path, 'rb') as f:
    file_data = f.read()
    file_name = f.name

msg.add_attachment(file_data,
                   maintype='application',
                   subtype='vnd.openxmlformats-officedocument.spreadsheetml'
                           '.sheet',
                   filename=file_name)

with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
    smtp.login(sender_email, app_password)
    smtp.send_message(msg)

print("Message was send")
