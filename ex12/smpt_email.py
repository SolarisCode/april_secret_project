import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
from_addr = "msearnold@gmail.com"
password = "iibuoowezaictitb"
to_addr = input("Enter the receiver email: ")
subject = input("Enter the subject: ")
message = input("Write the content of the message then press enter:\n")
file = input("Enter the absolute path for the attachment file: ")
file_des = input("Enter file description: ")

msg["From"] = from_addr
msg["To"] = to_addr
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))
attachment = open(file, "rb")

part = MIMEBase("application", "pdf")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(file_des, "attachment", filename=os.path.split(file)[-1])
msg.attach(part)

smtp_server = "smtp.gmail.com:587"
server = smtplib.SMTP(smtp_server)
server.ehlo()
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
attachment.close()
