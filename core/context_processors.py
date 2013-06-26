from .models import Pagina


def pagina_context_processors(request):
    pagina = Pagina.objects.latest('data_criacao')
    return {'pagina': pagina}
