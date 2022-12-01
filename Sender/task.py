from Mailganer.celery import app
import time
from datetime import datetime
from .models import Task, Email
from django.conf import settings
from django.core.mail import send_mail
from Template.models import Template
from Subscriber.models import Subscriber
from uuid import uuid1
from django.template.loader import render_to_string
import datetime as dt

 
    
@app.task    
def SendEmailManager(id = None):
    if id is None:
        qs = Task.objects.filter(complete_flag=False, start_time__gt=datetime.now())
        for task in qs:
            SendEmail.delay(task.id)
            
 
@app.task        
def SendEmail(id):
    task = Task.objects.get(id=id)
    sleep_time = 0 if task.start_now_flag == False else 1
    if task.start_now_flag == True:
        sleep_time = (task.start_time.replace(tzinfo=None) - datetime.now().replace(tzinfo=None)).total_seconds()
        if sleep_time >= 1:
            print(sleep_time)
            time.sleep(sleep_time)
    if (task.start_time.replace(tzinfo=None) + dt.timedelta(minutes=1)) >= datetime.now().replace(tzinfo=None):
        template = Template.objects.get(id=task.template.id)
        for sub in Subscriber.objects.all():
            d = dict({'name': '{fn} {ln}'.format(fn=sub.first_name, ln=sub.last_name),
                        'birthday': sub.birthday,
                        'id': uuid1(),
                        })
            msg_plain = render_to_string('email/{template_path}/index.txt'.format(template_path=template.template_path), d)
            msg_html = render_to_string('email/{template_path}/index.html'.format(template_path=template.template_path), d)
            send_mail('Title',
                    msg_plain,
                    settings.EMAIL_HOST_USER,
                    [sub.email],
                    html_message=msg_html,
                    )
            email = Email.objects.create(
                id=d['id'],
                task=task,
                subscruber=sub,
                opened=False,
            )
            email.save()
        task.complete_flag = True
        task.save()