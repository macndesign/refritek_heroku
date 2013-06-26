from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import Empresa, Pagina, Slider


class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeTemplateView, self).get_context_data(**kwargs)
        ctx['sliders'] = Slider.objects.ativos()
        ctx['empresas'] = Empresa.objects.ativos()
        ctx['pagina'] = get_object_or_404(Pagina, pk=1)
        return ctx
