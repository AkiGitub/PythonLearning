#sckd phda awgo nlau
import smtplib

App_Password = 'sckd phda awgo nlau'
from email.mime.text import MIMEText

subject = 'zogo'
body = 'body'
sender = 'unitydeveloper3d2@gmail.com'
rec = [sender,"akbarprogrammer@gmail.com"]

def send_email(subject, body, sender, recip):
    
    mes = MIMEText(body)
    mes['Subject'] = subject
    mes['From'] = sender
    mes['To'] = ','.join(rec)

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(sender,App_Password)
        smtp.sendmail(sender,recip,mes.as_string())
    
    print('___------------->')

send_email(subject,body,sender,rec)