import smtplib, ssl
import re
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# name = sys.argv[1]
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
name = sys.argv[1]
email = sys.argv[2]
message1 = sys.argv[3]
phone = sys.argv[4]

if(re.search(regex,str(email))):  
	print("YES")  
          
else:  
    print("NO")  
# message = str(sys.argv[3])
print(message1)
sender_email = ""
receiver_email = ""
password = ""
host = "smtp.gmail.com"
port = 465
message = MIMEMultipart("alternative")
message["Subject"] = "AgroAnalytics"
message["From"] = sender_email
message["To"] = receiver_email
text = "Name: {0}\nEmail: {1}\nPhone no: {3}\n{2}".format(name,email,message1,phone)

message.attach(MIMEText(text, "plain"))
context = ssl.create_default_context()
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
