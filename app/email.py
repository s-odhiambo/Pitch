from flask import Message
from flask import render_template
from . import mail



def mail_message(subject,template,to,**kwargs):
  sender_mail = 'samuelangienda1998@gmail.com'
  
  
  
  
  email = Messsage(subject, sender = sender_email, recipient = [to])
  email.body = render_template(template + ".text",**kwargs)
  email.html = render_template(template + ".html",**kwarg)
  mail.send(email) 