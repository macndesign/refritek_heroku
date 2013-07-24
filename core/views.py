from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from .models import Empresa, Pagina, Slider, Sobre, Contato, Cartao, Produto


class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeTemplateView, self).get_context_data(**kwargs)
        ctx['sliders'] = Slider.objects.ativos()
        ctx['produtos'] = Produto.objects.destaques()[:4]
        ctx['cartoes'] = Cartao.objects.ativos()
        ctx['pagina'] = get_object_or_404(Pagina, pk=1)
        return ctx


class EmpresaListView(ListView):
    queryset = Empresa.objects.ativos()
    context_object_name = 'empresas'
    template_name = 'core/empresas.html'


class ProdutoDetailView(DetailView):
    queryset = Produto
    template_name = 'core/produto.html'


class SobreTemplateView(TemplateView):
    template_name = 'core/sobre.html'

    def get_context_data(self, **kwargs):
        ctx = super(SobreTemplateView, self).get_context_data(**kwargs)
        ctx['sobre'] = get_object_or_404(Sobre, pk=1)
        ctx['cartoes'] = Cartao.objects.ativos()
        ctx['pagina'] = get_object_or_404(Pagina, pk=1)
        return ctx


class EmpresaDetailView(DetailView):
    model = Empresa
    template_name = 'core/produtos.html'

    def get_context_data(self, **kwargs):
        ctx = super(EmpresaDetailView, self).get_context_data(**kwargs)
        ctx['cartoes'] = Cartao.objects.ativos()
        ctx['pagina'] = get_object_or_404(Pagina, pk=1)
        return ctx


class ContatoTemplateView(TemplateView):
    template_name = 'core/contato.html'

    def get_context_data(self, **kwargs):
        ctx = super(ContatoTemplateView, self).get_context_data(**kwargs)
        ctx['contato'] = get_object_or_404(Contato, pk=1)
        ctx['cartoes'] = Cartao.objects.ativos()
        ctx['pagina'] = get_object_or_404(Pagina, pk=1)
        return ctx


class ForaDoArTemplateView(TemplateView):
    template_name = 'core/fora-do-ar.html'
