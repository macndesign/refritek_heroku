from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Empresa, Pagina, Slider, Sobre


class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeTemplateView, self).get_context_data(**kwargs)
        ctx['sliders'] = Slider.objects.ativos()
        ctx['empresas'] = Empresa.objects.ativos()
        ctx['pagina'] = get_object_or_404(Pagina, pk=1)
        return ctx


class SobreTemplateView(TemplateView):
    template_name = 'core/sobre.html'

    def get_context_data(self, **kwargs):
        ctx = super(SobreTemplateView, self).get_context_data(**kwargs)
        ctx['sobre'] = get_object_or_404(Sobre, pk=1)
        ctx['pagina'] = get_object_or_404(Pagina, pk=1)
        return ctx


class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'core/empresa.html'

    def get_context_data(self, **kwargs):
        ctx = super(EmpresaDetailView, self).get_context_data(**kwargs)
        ctx['pagina'] = get_object_or_404(Pagina, pk=1)
        return ctx


class ContatoTemplateView(TemplateView):
    template_name = 'core/contato.html'

    def get_context_data(self, **kwargs):
        ctx = super(ContatoTemplateView, self).get_context_data(**kwargs)
        ctx['pagina'] = get_object_or_404(Pagina, pk=1)
        return ctx
