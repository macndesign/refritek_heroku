from django.views.generic.base import TemplateView
from .models import Empresa, Produto, Slider


class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeTemplateView, self).get_context_data(**kwargs)
        ctx['sliders'] = Slider.objects.ativos()
        ctx['empresas'] = Empresa.objects.ativos()
        return ctx
