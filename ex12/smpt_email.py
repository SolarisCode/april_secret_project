import os
import ssl
import smtplib
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
from_addr = input("Enter your gmail: ")
password = getpass("Enter your password: ")
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

part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(file_des, f"attachment; file {os.path.split(file)[-1]}")
msg.attach(part)

# ssl_context = ssl.create_default_context()
smtp_server = "smtp.gmail.com:587"
server = smtplib.SMTP(smtp_server)
server.ehlo()
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
# with smtplib.SMTP_SSL(smtp_server, 465, context=ssl_context) as server:
#     server.login(from_addr, password)
#     server.sendmail(from_addr, to_addr, msg.as_string())
#     server.quit()
attachment.close()

