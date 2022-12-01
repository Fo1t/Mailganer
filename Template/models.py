# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from uuid import uuid1
# Create your models here.


class Template(models.Model):
    id = models.UUIDField(default=uuid1(), primary_key=True)
    template_path = models.CharField(max_length=100, blank=False, unique=True)
    template_name = models.CharField(max_length=50, blank=False, unique=True)
    
    def __str__(self):
        return '{name}'.format(name=self.template_name)