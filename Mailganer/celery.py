from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mailganer.settings')

app = Celery('Mailganer')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

app.config_from_object('django.conf:settings')
from django.conf import settings
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)