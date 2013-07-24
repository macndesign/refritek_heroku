from django.conf.urls import patterns, url
from .views import (HomeTemplateView, SobreTemplateView, EmpresaDetailView, ContatoTemplateView, EmpresaListView,
                    ProdutoDetailView)

urlpatterns = patterns('',
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^sobre/$', SobreTemplateView.as_view(), name='sobre'),
    url(r'^empresas/$', EmpresaListView.as_view(), name='empresas'),
    url(r'^empresa/(?P<pk>\d+)/$', EmpresaDetailView.as_view(), name='empresa'),
    url(r'^produto/(?P<pk>\d+)/$', ProdutoDetailView.as_view(), name='produto'),
    url(r'^contato/$', ContatoTemplateView.as_view(), name='contato'),
)
