from email.message import EmailMessage
import os
from dotenv import load_dotenv
import ssl
import smtplib
import zipfile
import glob

load_dotenv()

password = os.environ['PASSWORD']
email = os.environ['EMAIL']

email_sender = email
email_password = password
email_receiver = 'cenakat809@letpays.com'

subject = "Message important"
body = '''
    When you wathc a coding, please not surreder 
    and also send you a file of images
'''
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

#compres zip
with zipfile.ZipFile('E:/python-email/compres.zip','w') as f:
    for file in glob.glob('E:/mysimages/*'):
        f.write(file)

with open('E:/python-email/compres.zip','rb') as f:
    adjunto = f.read()

em.add_attachment(adjunto,maintype='aplication',subtype='zip',filename='compres.zip')


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())

