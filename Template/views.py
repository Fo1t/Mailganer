# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Template
from django.views.decorators.clickjacking import xframe_options_exempt


def TemplateMainPage(request):
    data = {
        'templates': Template.objects.all()
    }
    return render(request, 'templates.html', data)


@xframe_options_exempt
def template_frame(request, pk):
    data = {
        'name': 'First name Last name',
        'birthday': 'birthday'
    }
    return render(request, 'email/{}/index.html'.format(Template.objects.get(id=pk).template_path), data)
