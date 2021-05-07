# Trabalhando com formulários e Class Based View

Criar um arquivo Projeto\core\forms.py:

```python
from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_email(self):
        name = self.cleaned_data['Name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        body = f'Name: {name}\nE-mail:{email}\Subject: {subject}\n\
                    Message: {message}'
        mail = EmailMessage(
            subject=subject,
            body=body,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()

```

Em Projeto\core\views.py:

```python
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Service, Team
from .forms import ContactForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class= ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all() # faz carregar conteudos aleatório
        context['team'] = Team.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

class TesteView(TemplateView):
    template_name = 'teste.html'



```

Em Projeto\core\templates\contact.html:

```html

            <form id="contact" method="post" action='{% url "index" %}'>
              {% csrf_token %} <-- aqui -->
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <input type="text" class="form-control" id="name" name="name" placeholder="Name" required data-error="Please enter your name">
                    <div class="help-block with-errors"></div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group">
                    <input type="text" placeholder="Email" id="email" class="form-control" name="email" required data-error="Please enter your email">
                    <div class="help-block with-errors"></div>
                  </div> 
                </div>
                 <div class="col-md-12">
                  <div class="form-group">
                    <input type="text" placeholder="Subject" id="subject" class="form-control" name="subject" required data-error="Please enter your subject">
                    <div class="help-block with-errors"></div>
                  </div>
                </div>
                <div class="col-md-12">
                  <div class="form-group">
                    <textarea class="form-control" id="message" placeholder="Your Message" name="message" rows="7" data-error="Write your message" required></textarea>
                    <div class="help-block with-errors"></div>
                  </div>
                  <div class="submit-button text-left">
                    <button class="btn btn-common" id="form-submit" type="submit">Send Message</button>
                    <div id="msgSubmit" class="h3 text-center hidden"></div>
                    <div class="clearfix"></div>
                  </div>
                </div>
              </div>
            </form>
```

A única coisa feita seria renomear os 'id' e o 'name' para exatamente que se tem no
formulário ('Projeto\core\forms.py'). Se tiver tudo igual, o django vai pegar o que esta no
html e validar.


Em hero.html, acrescentar no rodapé:

```html

  <div class='container'>
      {% if messages %}
        {% message in messages %}
          <div class='alert alert-{{ message.tags }}'>
            <button type="button" class='close' data-dismiss='alert'></button>
            <strong>{{ message }} </strong>
          </div>
        {% endfor %}
      {% endif %}
  </div>

```

Em settings.py, acrescentar no final do arquivo:

```python

# Email de teste console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

"""
# Email produção

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'no-reply@fusion.com.br'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = 'fusion'
DEFAULT_FROM_EMAIL = 'contato@fusion.com.br'

"""

```