# coding: utf-8
from django.contrib import admin
from .models import Empresa, Pagina, Produto, Slider, Sobre, Contato
from south.models import MigrationHistory

admin.site.register(Empresa)
admin.site.register(Pagina)
admin.site.register(Produto)
admin.site.register(Slider)
admin.site.register(Sobre)
admin.site.register(Contato)
admin.site.register(MigrationHistory)
