# Traduzindo uma string na view

- Em Section_5_Django_Framework_avancado\Projeto (pasta raiz do projeto, na mesma pasta onde esta o manage.py) criar um diretório chamado locale (Section_5_Django_Framework_avancado\Projeto\locale)

- Ir em settings.py (Section_5_Django_Framework_avancado\Projeto\fusion\settings.py) e no final do arquivo acrescentar:

```python

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
```

E acrescentar na lista Middleware do arquivo settings.py:

```python

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware', # < --- Esse
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 'django.middleware.locale.LocaleMiddleware' automatiza a detecção de linguagem pelo 
# navegador.

```

Em views.py (Section_5_Django_Framework_avancado\Projeto\core\views.py):

```python
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
        lang = translation.get_language() # pega a linguagem do navegador
        context['services'] = Service.objects.order_by('?').all() # faz carregar conteudos aleatório
        context['team'] = Team.objects.order_by('?').all()
        context['lang'] = lang #
        translation.activate(lang) #
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, _('E-mail enviado com sucesso')) # colocou _(msg) que será traduzida
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar e-mail')) # colocou _(msg) que será traduzida
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


```

No template base (Section_5_Django_Framework_avancado\Projeto\core\templates\base.html) mudar o html lang = 'pt-br' para html lang = '{{ lang }} ':

```html
{% load static %}
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
```

Para traduzir em forms.py (Section_5_Django_Framework_avancado\Projeto\core\forms.py):

```python
from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _ #

class ContactForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100) #
    email = forms.EmailField(label=_('E-mail'), max_length=100) #
    subject = forms.CharField(label=_('Subject'), max_length=100) #
    message = forms.CharField(label=_('Message'), widget=forms.Textarea()) #

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        n = _('Name') #
        e = _('E-mail') #
        s = _('Subject') #
        m = _('Message') #

        body = f'{n}: {name}\n{e}:{email}\n{s}: {subject}\n\
                    {m}: {message}'
        mail = EmailMessage(
            subject=subject,
            body=body,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()
```

Para traduzir models.py (Section_5_Django_Framework_avancado\Projeto\core\models.py):

```python
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    created = models.DateField(_('Created'), auto_now_add=True)
    modified = models.DateField(_('Modified'), auto_now=True)
    active = models.BooleanField(_('Active?'), default=True)

    class Meta:
        abstract = True

class Service(Base):
    ICON_CHOICES=(
        ('lni-cog', _('Gear')),
        ('lni-stats-up', _('Graphic')),
        ('lni-users', _('Users')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Rocket'))
    )
    services = models.CharField(_('Services'), max_length=100)
    description = models.TextField(_('Description'), max_length=200)
    icon = models.CharField(_('Icon'), max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        return self.services

class Role(Base):
    role = models.CharField(_('Role'), max_length=100)

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self):
        return self.role

class Team(Base):
    name = models.CharField(_('Name'), max_length=100)
    role = models.ForeignKey('core.Role', verbose_name='Role', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    image = StdImageField(
        _('Image'),
        upload_to=get_file_path,
        variations={
        'thumbnail': {"width":480, "height":480, "crop":True}
        })
    facebook = models.CharField('Facebook', max_length=100, default="#")
    twitter = models.CharField('Twitter', max_length=100, default="#")
    instagram = models.CharField('Instagram', max_length=100, default="#")

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
    
    def __str__(self):
        return self.name
```



Para forms e models é indicado o gettext_lazy e para views é indicado o gettext.

No terminal:

```bash
\$ python manage.py makemessages -l es
processing locale es
(venv) 

```

Há diversas formas para fazer a tradução, pode ser manual no arquivo de extensão .po na pasta Section_5_Django_Framework_avancado\Projeto\locale\it\LC_MESSAGES) ou por meio da ferramenta chamada poedit.

Depois de feito a modificação no arquivo de tradução (extensão .po), é necessário compilá-lo:

```bash

python manage.py compilemessages
```