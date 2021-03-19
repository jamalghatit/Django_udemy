#  Enviando e-mails com Django

Configuração no settings.py

```python

# Configurações de email simulado:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#Imprimi o email no console, pois não há ainda o servidor de email.

# Configuração de servidor de email:
"""
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'no-reply@seudominio.com.br'
EMAIL_PORT = 587
EMAIL_USER_TSL = True
EMAIL_HOST_PASSWORD = 'sua senha'

"""
```

Alterar o core/forms.py

```python

from django import forms
from django.core.mail.message import EmailMessage

class ContatoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto:\
                    {assunto}\nMessagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo sistema django 2',
            body=conteudo,
            from_email="contato@seudominio.com.br",
            to=['contato@seudominio.com.br','outrocontato@seudominio.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()

```

Mudança no codigo views.py:

```python

def contato(request):
    form = ContatoForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Email enviado com sucesso!')
            form = ContatoForms()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    """
    Tudo aquilo que quiser enviar no contexto do template,
    é colocado nesse dicionário
    """
    context = {
        'form' : form
    }
    return render(request, 'contato.html', context=context)
```
