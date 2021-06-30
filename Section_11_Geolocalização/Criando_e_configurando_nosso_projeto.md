# Criando e configurando nosso projeto

Criar a Section_11_Geolocalização\geo, e instalar:
`pip install django geoip2 requests`

Criar o projeto e aplicação:

```python

django-admin startproject geo .
django-admin startapp core

```

Fazer o cadastro e download do [GeoLite2 City e o GeoLite2 Country](https://www.maxmind.com/en/accounts/574725/geoip/downloads)

Criar a pasta geoip em Section_11_Geolocalização\geo\geoip,

Extrair os arquivos .tar.gz que fora feito download e copiar de cada pasta extraída, o arquivo de extensão
.mmdb para a pasta geoip.

Entrar no site [yelp](https://www.yelp.com.br/s%C3%A3o-paulo) e se cadastrar. Após isso, entrar
na aba programadores (https://www.yelp.com.br/developers?country=US) e clicar na opção [Yelp Fusion](https://www.yelp.com.br/fusion), clicar em Get Started e preencher o formulário.

Depois de enviado o formulário, é gerado o client ID e a API Key. Elas são personalizadas, desse modo, não se deve passar a ninguem. Assim que terminar seu uso, será deletado.

```text
Client ID
iSGYVzOHomndqObjsJ1Gag

API Key
yvZdmYI3q4xarMaEzAkz8MukP7-s8OQJKEeXq3ZsiULOyJ-h_25741rPQImiwHeLsIcBh0Z3xKdMoj7u1WjS-3D57LoW08hIrL8CbVyRQiTJIfCfVPRXi__XVaHcYHYx
```

Em Section_11_Geolocalização\geo\geo\settings.py:

```python
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'core',
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
        'DIRS': ['templates'],
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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

YELP_API_KEY = 'yvZdmYI3q4xarMaEzAkz8MukP7-s8OQJKEeXq3ZsiULOyJ-h_25741rPQImiwHeLsIcBh0Z3xKdMoj7u1WjS-3D57LoW08hIrL8CbVyRQiTJIfCfVPRXi__XVaHcYHYx'

GEOIP_PATH = os.path.join(BASE_DIR,'geoip')

LOGOUT_REDIRECT_URL = 'index'

```
