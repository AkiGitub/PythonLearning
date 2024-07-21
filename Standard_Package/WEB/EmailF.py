from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib #
#mime= multi purpose  internet mail extension

mess = MIMEMultipart()
mess["from"] = "aki"
mess['to'] = 'm.akbar.jafari@gmail.com'
mess['subject'] = 'zogo'
mess.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp:
     smtp.ehlo()#hey i am client to want to send email
     smtp.starttls() #transport layer security to encrypt the message
     smtp.login('akbarprogrammer@gmail.com',"akbar22105")
                 
     smtp.send_message(mess)
     print('send...')
  