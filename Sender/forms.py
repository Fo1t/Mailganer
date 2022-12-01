from django import forms
from datetime import datetime, timedelta
from Template.models import Template

class SenderForm(forms.Form):
    start_time = forms.DateTimeField(initial=format(datetime.today(),'%Y-%m-%dT%H:%M'),input_formats=['%Y-%m-%dT%H:%M'], required=False)
    start_time.widget.attrs.update({'class': 'form-control', 'id': 'setting-input-1'})
    use_file = forms.BooleanField(initial=False, required=False)
    use_file.widget.attrs.update({'id': 'setting-input-2'})
    name = forms.CharField(max_length=50)
    name.widget.attrs.update({'class': 'form-control', 'type': 'text', 'id': 'setting-input-3'})
    file = forms.FileField(required=False)
    file.widget.attrs.update({'class': 'form-control', 'type': 'text', 'id': 'setting-input-4'})
    save_flag = forms.BooleanField(initial=True, required=False)
    save_flag.widget.attrs.update({'id': 'setting-input-5'})
    start_now_flag = forms.BooleanField(initial=False, required=False)
    start_now_flag.widget.attrs.update({'id': 'setting-input-6'})
    templates = forms.ModelChoiceField(
        queryset=Template.objects.all(),
        required=False,
        initial=Template.objects.first(),
    )
    