# Precisa fazer login com Facebook na sua aplicação? Vamos lá

- Criar ambiente virtual 
- Instalar django, social-auth-app-django, bootstrap4
- criar projeto facebook.
- Configurar o settings.py como nos projetos anteriores.

Section_12_Bonus\Aula_4_login_facebook\facebook\settings.py:

```python

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'bootstrap4',
    'social_django'
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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
    # Apenas se voce quiser manter a autenticação padrão do Django.
    'django.contrib.auth.backends.ModelBackend', 
]


```

Para saber configurar para outras plataformas de auth: https://python-social-auth.readthedocs.io/en/latest/backends/index.html

Criar pagina html - Section_12_Bonus\Aula_4_login_facebook\core\templates\base.html:

```html
{% load static %}
{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <meta http-equiv="X-UA-Compatible" content='ie=edge'>
        {% bootstrap_css %}
        <link rel="stylesheet" href="{% static 'css/style.css' %}" />
        <title>Django social</title>
    </head>
    <body>
        <div class="container-fluid">
            <div>
                <h1 class="text-white text-center">{% block title %}{% endblock %}</h1>
                <div class="card p-5">
                    {% block content %}{% endblock %}
                </div>
            </div>
        </div>
    {% bootstrap_javascript jquery='full'%}
    </body>
</html>
```

Criar pagina html - Section_12_Bonus\Aula_4_login_facebook\core\templates\login.html:

```html
{% extends 'base.html' %}
{% block title %}Logins{% endblock %}

{% block content %}

<div class="row">
    <div class="col-md-8 mx-auto social-container my-2 order-md-1">
        <button class="btn btn-primary mb-2">
            <a href="#">Login com Facebook</a>
        </button>
    </div>
</div>

{% endblock %}
```

Criar pagina html - Section_12_Bonus\Aula_4_login_facebook\core\templates\index.html:

```html

```
