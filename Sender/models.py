# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from uuid import uuid1
from Subscriber.models import Subscriber
from Template.models import Template

# Create your models here.

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1())
    start_time = models.DateTimeField(default=timezone.now(), blank=False)
    complete_flag = models.BooleanField(default=False, blank=False)
    name = models.CharField(max_length=50, blank=False, default='')
    start_now_flag = models.BooleanField(default=True, blank=False)
    template = models.ForeignKey(Template, blank=False, on_delete=models.CASCADE, related_name='task_template_related')
    
    def __str__(self):
        return '{name} {date}'.format(name=self.name, date=self.start_time.date)


class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid1())
    task = models.ForeignKey(Task, blank=False, related_name='email_task_related', on_delete=models.CASCADE)
    subscruber = models.ForeignKey(Subscriber, blank=False, related_name='email_sub_related', on_delete=models.CASCADE)
    opened = models.BooleanField(default=False, blank=False)