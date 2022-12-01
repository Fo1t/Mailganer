# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views import View
from Sender.forms import SenderForm
from uuid import uuid1, uuid4
import os
from .task import SendEmail
from .models import Task, Email
from datetime import datetime
from django.http import HttpResponse


def handle_uploaded_file(f, name):
    with open('files/{name}.txt'.format(name=name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def tracking(request, pk):
    email = Email.objects.get(id=pk)
    email.opened = True
    email.save()
    print('{} opened'.format(email.id))
    return HttpResponse('', 200)
    

class SenderView(View):
    
    def get(self, request):
        form = SenderForm()
        return render(request, 'sender.html', {'form': form})
    
    def post(self, request):
        form = SenderForm(request.POST, request.FILES)
        data = {}
        data['form.is_valid()'] = form.is_valid()
        data['form.errors'] = form.errors
        data['form.use_file'] = form.cleaned_data['use_file']
        data['form.start_now_flag'] = form.cleaned_data['start_now_flag']
        if form.is_valid():
            if form.cleaned_data['use_file']:
                id = uuid4()
                #handle_uploaded_file(request.FILES['file'], str(id))
                data['use_file'] = form.cleaned_data['use_file']
                data['file'] = form.cleaned_data['file']
            if form.cleaned_data['start_now_flag']:
                start_time = form.cleaned_data['start_time']
                data['start_now_flag'] = form.cleaned_data['start_now_flag']
                data['start_time'] = form.cleaned_data['start_time']
            data['name'] = form.cleaned_data['name']
            data['templates'] = form.cleaned_data['templates']
        print(data)
        id = uuid1()
        new_task = Task.objects.create(
            id=id,
            complete_flag=False,
            name=data['name'],
            start_now_flag=form.cleaned_data['start_now_flag'],
            template=form.cleaned_data['templates']
        )
        if form.cleaned_data['start_now_flag']:
            new_task.start_time = form.cleaned_data['start_time']
        #Task.objects.all().delete()
        new_task.save()
        SendEmail.delay(id)
        #print('start_time - {start_time}\n use_file - {use_file}\n name - {name}\n file - {file}\n save_flag - {save_flag}\n start_now_flag - {start_now_flag}'.format(start_time=form.cleaned_data['start_time'],use_file=form.cleaned_data['use_file'],name=form.cleaned_data['name'],file=form.cleaned_data['file'],save_flag=form.cleaned_data['save_flag'],start_now_flag=form.cleaned_data['start_now_flag']))
        #if form.is_valid():
        #    id = uuid4()
        #    print(213)
        #    handle_uploaded_file(request.FILES['file'], str(id))
        #    os.remove('files/{id}.txt'.format(id=id))
        return redirect('/')
        #return render(request, 'sender.html', {'form': form})
