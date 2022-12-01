from Stats.views import MainStatPage, StatInfo
from django.conf.urls import url

urlpatterns = [
    url('/(?P<pk>[-\w]+)/', StatInfo, name='stat_info'),
    url('$', MainStatPage, name='stats'),
]