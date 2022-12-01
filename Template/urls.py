from Template.views import TemplateMainPage, template_frame
from django.conf.urls import url

urlpatterns = [
    url('frame/(?P<pk>[-\w]+)/', template_frame, name='template_frame'),
    url('$', TemplateMainPage, name='template'),
]