# Precisa gerar gráficos na sua aplicação Django? Vamos lá!

Criar um novo projeto e ambiente virtual e instalar:

```bash
pip install django django-chartjs django-bootstrap4 

pip freeze > requirements.txt

django-admin startproject charts

django-admin startapp core
```

Depois fazer as configurações no Section_12_Bonus\Aula_1_charts\charts\charts\settings.py:

```python
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'bootstrap4',
    'chartjs',
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
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfile')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

```

Criar o arquivo de rotas na aplicação core Section_12_Bonus\Aula_1_charts\charts\core\urls.py:

```python
from django.urls import path

from .views import IndexView, DadosJASONView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dados/', DadosJASONView.as_view(), name='dados')
]
```

No arquivo de rotas do projeto Section_12_Bonus\Aula_1_charts\charts\charts\urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]
```

Criar o arquivo Index.html Section_12_Bonus\Aula_1_charts\charts\core\templates\index.html:

```html
{% load bootstrap4 %}
{% load static %}

<!doctype html>
<html lang="pt-br">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    {% bootstrap_css %}

    <title>Geek Charts</title>
  </head>
  <body>
    <div class="container">
        <h1 class="text-primary">Geek Charts</h1>
    </div>
    <div class="container">
        <canvas id="grafico" width="500" height="400"></canvas>
    </div>
    {% bootstrap_javascript jquery="full" %}
    <script type="text/javascript" src="{% static 'js/Chart.min.js' %}"></script>

    <script type="text/javascript">
        $.get('{% url "dados" %}', function(data){
            var ctx = $("#grafico").get(0).getContext("2d");
            new Chart(ctx, {
                type: 'line', data: data
            });
        });
    </script>
  </body>
</html>
```

Criar as views Section_12_Bonus\Aula_1_charts\charts\core\views.py:

