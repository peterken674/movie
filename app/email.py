from flask_mail import Message
from flask import render_template
from . import create_app, mail
import time

from .models import User



def mail_message(subject,template,to,**kwargs):
    sender_email = 'peter.kimani@student.moringaschool.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)

def send_recommendation(subject,template,to,**kwargs):
    sender_email = 'peter.kimani@student.moringaschool.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
    print('Email Sent')

def send_recommendation_at(send_time):
    subscribed_users = User.query.filter_by(subscribed=True)

    for user in subscribed_users:
        time.sleep(send_time.timestamp() - time.time())
        send_recommendation("Movie of the Day.", "email/recommendation", user.email, user = user)
        

