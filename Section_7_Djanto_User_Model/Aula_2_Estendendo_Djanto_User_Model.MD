# Estendendo o Django User Model

- Criar uma aplicação no projeto: `django-admin startapp core`

- Em settings.py (Projeto\django_user_model\django_user_model\settings.py):
  
```python

ALLOWED_HOSTS = ['*'] # add '*' na lista

INSTALLED_APPS = [
    'core', # add o app 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # add 'templates'
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

TIME_ZONE = 'America/Sao_Paulo' # mudar o fuso

# adicionar essas configurações 
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```


## Primeira forma de autenticação: via modelo do próprio do django.

Ir na aplicação e criar um model (Projeto\django_user_model\core\models.py).

```python
from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text', max_length=300)

    def __str__(self):
        return self.title

```

## Segunda forma de autenticação: criar seu modelo de usuario customizado

Em settings.py, add no final da linha:

```python

AUTH_USER_MODEL = 'usuarios.Custom'

```

E no models.py:

```python
from django.db import models

from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text', max_length=300)

    def __str__(self):
        return self.title

```

## Terceira forma e mais recomendada

E no models.py:

```python
from django.db import models

from django.contrib.auth import get_user_model

class Post(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name='Author', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Text', max_length=300)

    def __str__(self):
        return self.title

# Ela devolve o model do usuario. Se estiver sobrescrito la em settings por meio da variavel 
# AUTH_USER_MODEL = 'blabla', ele devolve esse model. Se não tiver sobrescrito, tras a nativa do 
# Django.
```

```bash
>>> get_user_model()
<class 'django.contrib.auth.models.User'>

```

Em Projeto\django_user_model\core\admin.py:

```python
from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
```

No bash:

```bash
\$ python manage.py makemigrations
\$ python manage.py migrate
\$ python manage.py createsuperuser
```

Em Projeto\django_user_model\core\admin.py:


```python

from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', '_author')
    #Para retornar um atributo da instancia.
    def _author(self, instance):
        return f'{instance.author.get_full_name()}'

```