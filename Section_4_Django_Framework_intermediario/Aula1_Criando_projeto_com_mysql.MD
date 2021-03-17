# Criando um novo projeto com MySQL

```bash
pip install django whitenoise gunicorn django-bootstrap4 pyMySQL django-stdimage
```

## whitenoise

**Radically simplified static file serving for Python web apps**

With a couple of lines of config WhiteNoise allows your web app to serve its own static files, making it a self-contained unit that can be deployed anywhere without relying on nginx, Amazon S3 or any other external service. (Especially useful on Heroku, OpenShift and other PaaS providers.)

It’s designed to work nicely with a CDN for high-traffic sites so you don’t have to sacrifice performance to benefit from simplicity.

WhiteNoise works with any WSGI-compatible app but has some special auto-configuration features for Django.

WhiteNoise takes care of best-practices for you, for instance:

Serving compressed content (gzip and Brotli formats, handling Accept-Encoding and Vary headers correctly)
Setting far-future cache headers on content which won’t change

## gunicorn

Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. It’s a pre-fork worker model ported from Ruby’s Unicorn project. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resource usage, and fairly speedy.

## django-bootstrap4

Bootstrap 4 integration for Django.

## pyMysql
PyMySQL is a pure-Python MySQL client library, based on PEP 249

## django-stdimage

Django Standarized Image Field

Django Field that implement the following features:

* Django-Storages compatible (S3)
* Resize images to different sizes
* Access thumbnails on model level, no template tags required
* Preserves original image
* Asynchronous rendering (Celery & Co)
* Restrict accepted image dimensions
* Rename files to a standardized name (using a callable upload_to)

---------------

## Criar o arquivo requirements.txt

```bash
pip freeze > requirements.txt
```

## Criar um novo projeto e uma nova aplicação

```bash
django-admin startproject django2 .

django-admin startapp core
```

## django2/settings.py

```bash
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', # aqui
    'bootstrap4', # aqui
    'stdimage', # aqui
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhitenoiseMiddleware', # aqui
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # AQUI
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # engine
        'NAME': 'django2',
        'USER': 'geek',
        'PASSWORD':'univesity',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo' 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

```
## Instalar MySQL server e o MySQL Workbench


> senha root mysql : university

e depois de instalar, conectar ao banco de dados via Workbench 
e criar um banco de dados:

```sql
create database django2;
```