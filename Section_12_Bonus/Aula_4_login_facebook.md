# Precisa fazer login com Facebook na sua aplicação? Vamos lá

- Criar ambiente virtual 
- Instalar django,  social-auth-app-django, django-bootstrap4
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
            <a href="{% url 'social:begin' 'facebook' %}">Login com Facebook</a>
        </button>
    </div>
</div>

{% endblock %}
```

Criar pagina html - Section_12_Bonus\Aula_4_login_facebook\core\templates\index.html:

```html


{% extends 'base.html' %}
{% block title %}Início{% endblock %}
{% block content %}
<div class="row">
    <div class="col-sm-12 mb-3">
        <h4 class="text-center">Bem-vindo(a) {{ user.username }} </h4>
    </div>

    {% for a in backends.associated %}
        {% if a.provider == 'facebook' %}
            <div class="col-md-4 text-center">
                <img src="{{ a.extra_data.picture.data.url }}" alt="" width="130" height="130" style="border-radius: 50%;">
            </div>
            <div class="col-md-8 social-container my-2">
                <p>Logado via: {{ a.provider|title }}</p>
                <p>Nome: {{ a.extra_data.name }}</p>
                <p>Profile: <a href="{{ a.extra_data.profile_url }}">Link</a></p>
            </div>
        {% endif %}
    {% endfor %}
    <div class="col-sm-12 mt-2 text-center">
        <button class="btn btn-warning">
            <a href="{% url 'logout' %}">Logout</a>
        </button>
    </div>
</div>
{% endblock %}
```

- Criar o diretório static\css (Section_12_Bonus\Aula_4_login_facebook\core\static\css) e criar dentro dele o arquivo style.css

```css

img {
    border: 3px solid #282c34;
}

.container-fluid {
    height: 100vh;
    background-color: #282c34;
    display: flex;
    justify-content: center;
    align-items: center;
}

.container-fluid > div {
    width: 85%;
    min-width: 300px;
    max-width: 500px;
}

.card {
    width: 100%;
}

.social-container{
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.btn a, .btn a:hover{
    color: white;
    text-decoration: none;
}

```

Em Section_12_Bonus\Aula_4_login_facebook\core\views.py:

```python

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
class LoginView(TemplateView):
    template_name = 'login.html'

```

Em Section_12_Bonus\Aula_4_login_facebook\facebook\urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

Criar um arquivo urls.py (Section_12_Bonus\Aula_4_login_facebook\core\urls.py) contendo:

```python
from django.urls import path, include
from django.contrib.auth import views as auth_views

from core.views import IndexView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', IndexView.as_view(), name='index'),
]

```

Em settings.py (Section_12_Bonus\Aula_4_login_facebook\facebook\settings.py):

```python

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'

# Configurações para facebook

SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_FACEBOOK_KEY = '' # ID do aplicativo
SOCIAL_AUTH_FACEBOOK_SECRET = ''
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, picture.type(large), link'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA =[
    ('name', 'name'), 
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]
```


