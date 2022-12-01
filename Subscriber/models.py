# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.db import models
from uuid import uuid1

# Create your models here.
class Subscriber(models.Model):
    id = models.UUIDField(default=uuid1(), primary_key=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    birthday = models.DateField(default=date.today(), blank=True)
    email = models.EmailField(blank=False, unique=True)