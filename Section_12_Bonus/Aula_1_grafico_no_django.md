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

```python

from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJASONView(BaseLineChartView):
    
    def get_labels(self):
        """Retorna 12 labels para a representação do x"""
        labels = [
            "Janeiro",
            "Fevereiro",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]
        
        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets."""
        datasets = [
            "Programação para Leigos",
            "Algoritmos e lógica de programação",
            "Programação em C",
            "Porgramação em Java",
            "Programação em Python",
            "Banco de dados"
        ]
        return datasets
    
    def get_data(self):
        """
        Retorna 6 datasets para plotar o grafico

        Cada linha representa um dataset
        Cada coluna representa um label
        
        A quantidade de dados precisa ser igual aos datasets/Labels
        
        12 labels, então 12 colunas,
        6 datasets, então 6 linhas.

        """

        dados = []
        for linhas in range(6):
            for colunas in range(12):
                dado = [
                    randint(1,200), # jan
                    randint(1,200), # fev
                    randint(1,200), # mar
                    randint(1,200), # abr
                    randint(1,200), # mai
                    randint(1,200), # jun
                    randint(1,200), # jul
                    randint(1,200), # ago
                    randint(1,200), # set
                    randint(1,200), # out
                    randint(1,200), # nov
                    randint(1,200), # dez
                ]
            dados.append(dado)
        return dados
```