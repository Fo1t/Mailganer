# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Template

# Register your models here.

class TemplateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Template, TemplateAdmin)