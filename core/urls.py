from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name='home'),
)