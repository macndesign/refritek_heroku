# coding: utf-8
from django.conf import settings
from django.shortcuts import render

class ForaDoArMiddleware(object):
    def process_request(self, request):
        if settings.FORA_DO_AR:
            return render(request, 'core/fora-do-ar.html')
        else:
            pass
