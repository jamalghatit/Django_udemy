from django.shortcuts import render

from django.views.generic import TemplateView
from django.utils.safestring import mark_safe # remove strings inseguras
import json

class IndexView(TemplateView):
    template_name = 'index.html'


class SalaView(TemplateView):
    template_name = 'sala.html'

    def get_context_data(self, **kwargs):
        context = super(SalaView, self).get_context_data(**kwargs)
        context['nome_sala_json'] = mark_safe(
            json.dumps(self.kwargs['nome_sala']) # pega o arquivo e transforma em um json
        )
        return context

