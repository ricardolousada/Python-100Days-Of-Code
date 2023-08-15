# Created by Ricardo Lousada
import smtplib, ssl

SMTP_SERVER = "smtp.gmail.com"
PORT = 587
SENDER_EMAIL= "lousadaricardo5@gmail.com"
SENDER_PASSWORD ="vkqabtgyjoxdyhzo"


#create a secure SSL context
context = ssl.create_default_context()

# Try log in to server and send e-mail
try:
    server = smtplib.SMTP(SMTP_SERVER,PORT)
    server.starttls(context=context)
    server.login((SENDER_EMAIL,SENDER_PASSWORD))
    server.sendmail(SENDER_EMAIL,"ricardo.lousada@gmail.com",msg="Hello")
except Exception as error:
    print(error)
finally:
    server.quit()
