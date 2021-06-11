# Relacionamento um para um

- Criar um virtual env e um novo projeto na pasta (Section_9_Relacionamento_entre_modelos\django-orm).

```bash
# criar ambiente virtual
\$ python -m venv venv
$ source venv/Scripts/activate

# instalar o django
$ pip install django

# Criar projeto
$ django-admin startproject django_orm .
$ django-admin startapp core

```

Ir em Section_9_Relacionamento_entre_modelos\django_orm\django_orm\settings.py:

```python

# add a aplicação
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', #
]

# Indicar o diretório da pasta template
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], #
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Mudar a região:
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


```

Em Section_9_Relacionamento_entre_modelos\django_orm\core\models.py:

```python
from django.db import models

class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Max 16 caracteres')

    class Meta:
        verbose_name: 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero

class Carro(models.Model):
    """
    Cada carro só pode se relacionar com um Chassi
    Cada Chassi só pode se relacionar com um carro.
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=32, help_text='Max 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return self.modelo
```

Em Section_9_Relacionamento_entre_modelos\django_orm\core\admin.py:

```python

from django.contrib import admin

from .models import Chassi, Carro

@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('numero', )

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'chassi', 'preco')

```

Agora que fez os modelos, aplicar fazer as migrações e aplicar:

```bash

\$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py createsuperuser
# geek geek

```

Django-shell `./manage.py shell`:

```python

>>> from core.models import Carro
>>> carro = Carro.objects.all()
>>> carro
<QuerySet [<Carro: Honda City>]>
>>> type(carro)
<class 'django.db.models.query.QuerySet'>

# Somente o tipo QuerySet tem esse metodo query.
>>> print(carro.query)
SELECT "core_carro"."id", "core_carro"."chassi_id", "core_carro"."modelo", "core_carro"."preco" FROM "core_carro"

>>> carro = Carro.objects.get(pk=2)
>>> type(carro)
<class 'core.models.Carro'>

>>> carro.preco
Decimal('60000.00')
>>> carro.chassi
<Chassi: 323232323232>
>>> chassi = carro.chassi
>>> chassi
<Chassi: 323232323232>
>>> type(chassi)
<class 'core.models.Chassi'>



```
