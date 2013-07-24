# coding: utf-8
from django.contrib import admin
from .models import Empresa, Pagina, Produto, Slider, Sobre, Contato, Cartao
from south.models import MigrationHistory


class ProdutoAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'empresa']
    list_display = ['nome', 'empresa', 'destaque', 'ativo']

admin.site.register(Produto, ProdutoAdmin)

admin.site.register(Empresa)
admin.site.register(Pagina)
admin.site.register(Slider)
admin.site.register(Sobre)
admin.site.register(Contato)
admin.site.register(Cartao)
admin.site.register(MigrationHistory)
