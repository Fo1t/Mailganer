# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from Sender.task import SendEmailManager


class SenderConfig(AppConfig):
    name = 'Sender'
    verbose_name = 'Send Email Manager'
    def ready(self):
        SendEmailManager.delay()
