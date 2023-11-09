import smtplib

mailFrom = 'Your Automation system'
mailTo = 'wojciechwierzbicki89@gmail.com'
mailSubject = 'This is a Test'
mailBody = '''Hi 
This is a test of how to send email from Python to a selected user
Yes, you're welcome'''

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)
user = 'wojciechwierzbicki89@gmail.com'
password = ']           '

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('Error')
