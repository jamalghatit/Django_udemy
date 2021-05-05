from django.views.generic import TemplateView

from .models import Service, Team

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all() # faz carregar conteudos aleatório
        context['team'] = Team.objects.order_by('?').all()
        return context

class TesteView(TemplateView):
    template_name = 'teste.html'

