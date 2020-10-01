import smtplib

SERVER = ('smtp.gmail.com')

FROM = "sender@gmail.com"
password="sender-password"

TO = ["reciver-mail"] # must be a list

SUBJECT = "OPERATION TEAM"

TEXT = (" DEPLOYMENT IS SCCESSFULL")

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.starttls() 
server.login(FROM, password) 
server.sendmail(FROM, TO, message)
server.quit()
