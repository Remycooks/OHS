from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import random
import os


def send_mail(subject,text, email):
    smtp = smtplib.SMTP('Smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('knk.seproject@gmail.com', 'siqv nrsn rtpa fchu')
    number = random.randint(1111,9999)
    otp=str(number)
    msg = MIMEMultipart()
    msg['Subject'] = subject
    text=text+"\n"+"otp : "+otp
    msg.attach(MIMEText(text))
    smtp.sendmail(from_addr="knk.seproject@gmail.com",to_addrs=email, msg=msg.as_string())
    smtp.quit()
    return number

def send_confirmation_mail(subject,text, email):
    smtp = smtplib.SMTP('Smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('knk.seproject@gmail.com', 'siqv nrsn rtpa fchu')
    
    msg = MIMEMultipart()
    msg['Subject'] = subject
    text="Your Booking Has been confirmed"+"\n"+ "Details of booking :"+ "\n" + text
    msg.attach(MIMEText(text))
    smtp.sendmail(from_addr="knk.seproject@gmail.com",to_addrs=email, msg=msg.as_string())
    smtp.quit()

def send_cancellation_mail(subject,text, email):
    smtp = smtplib.SMTP('Smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('knk.seproject@gmail.com', 'siqv nrsn rtpa fchu')
    
    msg = MIMEMultipart()
    msg['Subject'] = subject
    text="Your Booking Has been cancelled"+"\n"+ "Details of booking :"+ "\n" + text
    msg.attach(MIMEText(text))
    smtp.sendmail(from_addr="knk.seproject@gmail.com",to_addrs=email, msg=msg.as_string())
    smtp.quit()

    

