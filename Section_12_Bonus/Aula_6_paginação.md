# Trabalhando com paginação no Django

## Criando e configurando o ambiente

- Criar ambiante virtual em Aula_6_paginação
- Instalar o django==2.2.8 (django LTS), django-bootstrap4 e depois pip freeze
  
```bash
pip install django==2.2.8 django-bootstrap4

pip freeze > requirement.txt
```

- Criar projeto `django-admin startproject paginacao`
- Criar aplicação ` django-admin startapp core`

- Em Aula_6_paginação\paginacao\paginacao\settings.py:

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
```

- Em Aula_6_paginação\paginacao\core\models.py:

```python
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

```

- No bash, fazer a migração e depois aplicá-la:

```python
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```

- Em Aula_6_paginação\paginacao\core\admin.py:

```python
from django.contrib import admin

from core.models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco']

```

- Em Aula_6_paginação\paginacao\core\views.py:

```python
from django.views.generic import ListView

from core.models import Produto

class IndexListView(ListView):
    template_name = 'index.html'
    model = Produto
    paginate_by = 2
    ordering = 'id'

```

- Criar diretório templates e criar o Aula_6_paginação\paginacao\core\templates\index.html:

```html

{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        {% bootstrap_css %}
        <title>Paginação Django</title>
    </head>
    <body>
        <div class="container">
            <h1>Produtos</h1>
        </div>
        <div class="container">
            <table class="table">
                <thead>
                    <tr scope="col">#</tr>
                    <tr scope="col">Nome</tr>
                    <tr scope="col">Preço</tr>
                </thead>

                <tbody>
                    {% for p in page_obj %} <!--Como esta trabalhando com paginação, ao inves de ser chamado Produto, se chama page_obj-->
                        <tr>
                            <th scope="row">{{ p.id }}</th>
                            <th scope="row">{{ p.nome }}</th>
                            <th scope="row">{{ p.preco }}</th>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
            {% if is_paginated %}
                <nav aria-label="navegacao-paginacao">
                    <ul class="pagination">
                        {% if page_obj.has_previous %}
                            <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">&laquo;</a></li>
                        {% else %}
                            <li class="page-item disabled"><a class="page-link" href="#">&laquo;</a></li> 
                        {% endif %}

                        {% for num in paginator.page_range %}
                            {% if page_obj.number == num %}
                                <li class="page-item active"><a class="page-link" href="#" >{{ num }}</a> </li>
                            {% else %}
                                <li class="page-item"><a class="page-link" href="?page={{ num }}">{{ num }}</a> </li>
                            {% endif %}
                        {% endfor %}

                        {% if page_obj.has_next %}
                            <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">&raquo;</a></li>
                        {% else %}
                            <li class="page-item disabled"><a class="page-link" href="#">&raquo;</a></li> 
                        {% endif %}
                    </ul>
                </nav>
            {% endif %}
        </div>
        {% bootstrap_javascript jquery='full' %}
    </body>
</html>

```

- Em Aula_6_paginação\paginacao\paginacao\urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    
]
```

- Em Aula_6_paginação\paginacao\core\urls.py:

```python
from django.urls import path

from .views import IndexListView

urlpatterns = [
    path('', IndexListView.as_view(), name='index')
]
```

Para aproveitar o codigo em outros projetos, dividir o codigo da paginação em outro html

Em Aula_6_paginação\paginacao\core\templates\index.html:

```html

{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        {% bootstrap_css %}
        <title>Paginação Django</title>
    </head>
    <body>
        <div class="container">
            <h1>Produtos</h1>
        </div>
        <div class="container">
            <table class="table">
                <thead>
                    <tr scope="col">#</tr>
                    <tr scope="col">Nome</tr>
                    <tr scope="col">Preço</tr>
                </thead>

                <tbody>
                    {% for p in page_obj %} <!--Como esta trabalhando com paginação, ao inves de ser chamado Produto, se chama page_obj-->
                        <tr>
                            <th scope="row">{{ p.id }}</th>
                            <th scope="row">{{ p.nome }}</th>
                            <th scope="row">{{ p.preco }}</th>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
            
            {% include 'paginacao.html' %} <!-- Inclui o codigo dessa pagina -->
            
        </div>
        {% bootstrap_javascript jquery='full' %}
    </body>
</html>


``` 

Em Aula_6_paginação\paginacao\core\templates\paginacao.html:

```python
{% if is_paginated %}
    <nav aria-label="navegacao-paginacao">
        <ul class="pagination">
            {% if page_obj.has_previous %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">&laquo;</a></li>
            {% else %}
                <li class="page-item disabled"><a class="page-link" href="#">&laquo;</a></li> 
            {% endif %}

            {% for num in paginator.page_range %}
                {% if page_obj.number == num %}
                    <li class="page-item active"><a class="page-link" href="#" >{{ num }}</a> </li>
                {% else %}
                    <li class="page-item"><a class="page-link" href="?page={{ num }}">{{ num }}</a> </li>
                {% endif %}
            {% endfor %}

            {% if page_obj.has_next %}
                <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">&raquo;</a></li>
            {% else %}
                <li class="page-item disabled"><a class="page-link" href="#">&raquo;</a></li> 
            {% endif %}
        </ul>
    </nav>
{% endif %}
```