# Criando um novo projeto com PostgreSQL

- Criar um ambiente virtual: `python -m venv venv`
- Instalar os pacotes python:

`pip install django psycopg2-binary gunicorn dj-static django-stdimage`


psycopg2-binary: biblioteca python para banco de dados PostgreSQL
gunicorn: rodar o projeto
dj-static: para os arquivos estaticos
django-stdimage: auxilia para trabalhar com imagens no django.

- Criar o requirements.txt: `pip freeze > requirements.txt`
- Criar aplicação na pasta fusion

```bash

$ django-admin startproject fusion .
(venv)

```

- Criar aplicativo core:

```bash

$ django-admin startapp core
(venv)

```

- Ir em fusion/settings.py:

```python

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # colocar asterisco


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'core', # add nossa aplicação
    
]

```

- criar as pastas static e templates na pasta core.

```python 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # colocar aqui o nome do diretório de templates 
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

# Modificar o dicionario databases para o uso do postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fusion',
        'USER': 'geek',
        'PASSWORD': 'university',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

- Em fusion/url.py:

```python

from django.urls.static import static
from django.conf import settings

# Ao importar o django.conf.settings, isso permite que 
# a aplicação busque dados do settings, ou seja, 
# as variaveis media_url e media_root serão
# buscados do arquivo settings.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


```

- Criar arquivo urls.py em core:

```python

from django.urls import path

urlpatterns = [

]

```

```text
usuário para conexão:

usuario: postgres
senha: postgres
```

- Abrir o pgadmin e criar um usuário 'geek' com a senha 'university', bem como
criar um banco de dados chamado fusion.


```sql

CREATE ROLE geek WITH
  LOGIN
  SUPERUSER
  INHERIT
  CREATEDB
  CREATEROLE
  NOREPLICATION
  ENCRYPTED PASSWORD 'SCRAM-SHA-256$4096:VJf7pLmlAYkeN/tfPSm3XQ==$A9eucR5HBz6hxi7Fny9v/NO9RLD/Vg/rV2NrZBHuGdg=:UPdZMtSYcyn0srVKSoWtHOpQB0nYnqvt2eHSmb+cjD0=';

CREATE DATABASE fusion
    WITH
    OWNER = geek
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

```
