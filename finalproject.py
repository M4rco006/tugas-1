import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication

#data-data email
email_sender = input(str("From: "))
email_password = input(str("Input password: "))
email_reciever = input(str("To: "))

#subject email
message = MIMEMultipart()
message['From'] = email_sender
message['To'] = email_reciever
message['Subject']=input(str("Email subject: "))

#isi email
body_email = input(str("Email content: "))
message.attach(MIMEText(body_email,'plain'))

#attachment
# file_attach = MIMEApplication(open('attachment.txt','rb').read())
# file_attach.add_header('Content-Disposition', 'attachment', filename='attachment.txt')
# message.attach(file_attach)

#pengiriman
try:
    print("Sending email...")
    session = smtplib.SMTP_SSL('smtp.gmail.com',465)
    session.ehlo()
    session.login(email_sender, email_password)
    text = message.as_string()
    session.sendmail(email_sender,email_reciever, text)
    session.quit()
    print('Email sent, check your inbox')
except Exception as exception:
    print("Error: %s!\n\n" % exception)

#refrensi: https://github.com/kopper168/final_project