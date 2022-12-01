from Sender.views import SenderView, tracking
from django.conf.urls import url

urlpatterns = [
    url('', SenderView.as_view(), name='Sender'),
    url('tracking/(?P<pk>[-\w]+)', tracking, name='tracking'),
]