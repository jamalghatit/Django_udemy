# 87. Criando o projeto, a aplicação e configurando o Django Channels

Criar um ambiente virtual e instalar:

```bash
pip install django channels django-bootstrap4 channels-redis
django-admin startproject realtime .
django-admin startapp chat
```

Redis é um banco de dados que possibilita realizar aplicações em realtime.

Section_10_Trabalhando_com_Aplicações_em_tempo_real\realtime\settings.py:

```python

ALLOWED_HOSTS = ['*'] # colocar asterisco


# Application definition

INSTALLED_APPS = [
    'bootstrap4', # add os apps
    'channels', # add os apps
    'chat', # add os apps
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
        'DIRS': ['templates'], # diretório de templates
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

LANGUAGE_CODE = 'pt-br' # mudar para pt br

TIME_ZONE = 'America/Sao_Paulo' # mudar para isso

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Especifica do Channels
# ASGI é para aplicações em tempo real, o WSGI não suporta esse tipo de operação.
ASGI_APPLICATION = 'realtime.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('192.168.15.27', 6379)]
        },
    },

}
```

No linux onde fora instalado o redis-server `apt-get install redis-server`
Abra o arquivo de configuração /etc/redis/redis.conf e altere para:

bind 0.0.0.0 ::1
protected-mode no

e depois o inicie no bash:
`redis-server --protected-mode no`