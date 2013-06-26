from .models import Pagina
from django.shortcuts import get_object_or_404


def pagina_context_processors(request):
    pagina = None

    if Pagina.objects.latest('data_criacao'):
        pagina = Pagina.objects.latest('data_criacao')
        pagina = get_object_or_404(pagina)

    return {'pagina': pagina}
