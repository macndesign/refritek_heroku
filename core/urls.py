from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import HomeTemplateView, SobreTemplateView, EmpresaDetailView, ContatoTemplateView

urlpatterns = patterns('',
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^sobre/$', SobreTemplateView.as_view(), name='sobre'),
    url(r'^empresa/(?P<pk>\d+)/$', EmpresaDetailView.as_view(), name='empresa'),
    url(r'^contato/$', ContatoTemplateView.as_view(), name='contato'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
