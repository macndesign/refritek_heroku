from .models import Pagina
from django.shortcuts import get_object_or_404


def pagina_context_processors(request):
    pagina = get_object_or_404(Pagina)
    return {'pagina': pagina}
