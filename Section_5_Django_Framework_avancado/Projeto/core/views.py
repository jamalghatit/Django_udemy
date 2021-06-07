from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _ # 
from django.utils import translation # 

from .models import Service, Team
from .forms import ContactForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class= ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language() 
        context['services'] = Service.objects.order_by('?').all()
        context['team'] = Team.objects.order_by('?').all()
        context['lang'] = lang #
        translation.activate(lang) #
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, _('E-mail enviado com sucesso')) 
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar e-mail')) 
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

class TesteView(TemplateView):
    template_name = 'teste.html'

