# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Sender.models import Task, Email
from datetime import datetime

# Create your views here.
def MainStatPage(request):
    success_task = []
    for task in Task.objects.filter(complete_flag=True):
        success_task.append({
            'task': task,
            'count': len(Email.objects.filter(task=task)),
        })
    error_task = []
    for task in Task.objects.all():
        if (task.start_time.replace(tzinfo=None) < datetime.now().replace(tzinfo=None)) and (task.complete_flag == False):
            error_task.append({
                'task': task,
                'count': len(Email.objects.filter(task=task)),
            })
    waiting_task = []
    for task in Task.objects.filter(complete_flag=False, start_time__gt=datetime.now()):
        waiting_task.append({
            'task': task,
            'count': len(Email.objects.filter(task=task)),
        })
    all_task = []
    status_class = ''
    status_msg = ''
    for task in Task.objects.all():
        if (task.start_time.replace(tzinfo=None) < datetime.now().replace(tzinfo=None)) and (task.complete_flag == False):
            status_class = 'badge bg-danger'
            status_msg = 'Ошибка'
        if (task.start_time.replace(tzinfo=None) > datetime.now().replace(tzinfo=None)):
            status_class = 'badge bg-warning'
            status_msg = 'В ожидании'
        if task.complete_flag:
            status_class = 'badge bg-success'
            status_msg = 'Завершено'
        all_task.append({
            'task': task,
            'count': len(Email.objects.filter(task=task)),
            'status_class': status_class,
            'status_msg': status_msg,
        })
    data = {
        'success_task': success_task,
        'error_task': error_task,
        'waiting_task': waiting_task,
        'all_task': all_task,
    }
    return render(request, 'stats_all.html', data)



def StatInfo(request, pk):
    task = Task.objects.get(id=pk)
    emails = []
    for email in Email.objects.filter(task=task):
        emails.append({
            'sub': email.subscruber.email,
            'count': len(Email.objects.filter(subscruber=email.subscruber, task=task)),
            'interest': (len(Email.objects.filter(subscruber=email.subscruber, opened=True)) / len(Email.objects.filter(subscruber=email.subscruber))) * 100
        })
    data = {
        'task': task,
        'emails': emails,
        'count': len(Email.objects.filter(task=task)),
        'open_count': len(Email.objects.filter(task=task, opened=True)),
    }
    return render(request, 'stat_detail.html', data)