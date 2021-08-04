# Criando um CRUD com Class Based View

## Criando e configurando o ambiente

- Criar ambiante virtual em Aula_5_CRUD_Class_Based_View
- Instalar o django==2.2.8 (django LTS), django-bootstrap4 e depois pip freeze
  
```bash
pip install django==2.2.8 django-bootstrap4

pip freeze > requirement.txt
```

- Criar projeto `django-admin startproject crudcbv`
- Criar aplicação ` django-admin startapp core`

- Criar pasta templates em Aula_5_CRUD_Class_Based_View\crudcbv\core\templates

- Criar o arquivo Aula_5_CRUD_Class_Based_View\crudcbv\core\urls.py
  
- Em Aula_5_CRUD_Class_Based_View\crudcbv\core\models.py:

```python
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
```

- Em Aula_5_CRUD_Class_Based_View\crudcbv\core\admin.py:
  
```python
from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

```

- Em Aula_5_CRUD_Class_Based_View\crudcbv\crudcbv\settings.py:

```python

ALLOWED_HOSTS = ['*'] #


# Application definition

INSTALLED_APPS = [
    'core', # app
    'bootstrap4', # bootstrap4
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', # ajuda na configuração de pontuação
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # 
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

LANGUAGE_CODE = 'pt-br' #

TIME_ZONE = 'America/Sao_Paulo' #

```

- No bash:

```bash

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser
```

- Em Aula_5_CRUD_Class_Based_View\crudcbv\core\forms.py:

```python
from django import forms

from .models import Produto

class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'

```

## List

- Em Aula_5_CRUD_Class_Based_View\crudcbv\core\views.py:

```python
from django.db import models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Produto
from .forms import ProdutoModelForm


class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all() # qual consulta quer fazer no banco de dados.
    context_object_name = 'produtos'

```

- Em Aula_5_CRUD_Class_Based_View\crudcbv\crudcbv\urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]

```

Em Aula_5_CRUD_Class_Based_View\crudcbv\core\urls.py:

```python
from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),    
]
```

Em Aula_5_CRUD_Class_Based_View\crudcbv\core\templates, criar base.html:

```html
{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        {% bootstrap_css %}
        <title>CRUD CBV</title>
    </head>
    <body>
        <div class='container'>
            {% block content %} {% endblock %}
        </div>
    
    {% bootstrap_javascript jquery='full' %}
    </body>
</html>

```

Em Aula_5_CRUD_Class_Based_View\crudcbv\core\templates, criar index.html:

```html
{% extends "base.html" %}
{% load humanize %}

{% block content %}
    <div class ="row">
        <h1>Produto</h1>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Nome</th>
                    <th scope="col">Preço</th>
                    <th scope="col">Ação</th>
                </tr>
            </thead>
            <tbody>
                {% for produto in produtos %}
                <tr> <!--Linha-->
                    <td >{{ produto.id }}</td> <!--celulas do registro-->
                    <td>{{ produto.nome }}</td>
                    <td>R$ {{ produto.preco|intcomma }}</td> <!--intcommma formata os numeros conforme a idioma-->
                    <td>
                        <a class="btn btn-warning" href="#">Editar</a>
                        <a class="btn btn-danger" href="#">Deletar</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
```

## Create

- Em Aula_5_CRUD_Class_Based_View\crudcbv\core\views.py:

```python
from django.db import models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto
from .forms import ProdutoModelForm


class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all() # qual consulta quer fazer no banco de dados.
    context_object_name = 'produtos'
    
class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

```

Em Aula_5_CRUD_Class_Based_View\crudcbv\core\templates\produto_form.html:

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
    <h1>Produto</h1>
    <form method="post">
        {% csrf_token %}
        {% bootstrap_form form %}
            {% buttons %}
                <button type="submit" class="btn btn-primary">Salvar</button>
                <button type="button" class="btn btn-warning">
                    <a href="{% url 'index' %}">Cancelar</a>
                </button>
            {% endbuttons %}
    </form>
{% endblock %}

```

Em Aula_5_CRUD_Class_Based_View\crudcbv\core\urls.py:

```python
from django.urls import path

from .views import IndexView, CreateProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),    
    path('add/', CreateProdutoView.as_view(), name='add_produto')
]
```

## Update

- Em Aula_5_CRUD_Class_Based_View\crudcbv\core\views.py:

```python
from django.db import models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto
from .forms import ProdutoModelForm


class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all() # qual consulta quer fazer no banco de dados.
    context_object_name = 'produtos'
    
class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')
```

Em Aula_5_CRUD_Class_Based_View\crudcbv\crudcbv\urls.py:

```python
from django.urls import path

from .views import IndexView, CreateProdutoView, UpdateProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),    
    path('add/', CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/update', UpdateProdutoView.as_view(), name='upd_produto')
]
```

Em Aula_5_CRUD_Class_Based_View\crudcbv\core\templates\index.html:

```html
{% extends "base.html" %}
{% load humanize %}

{% block content %}
    <div class ="row">
        <h1>Produto</h1>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Nome</th>
                    <th scope="col">Preço</th>
                    <th scope="col">Ação</th>
                </tr>
            </thead>
            <tbody>
                {% for produto in produtos %}
                <tr> <!--Linha-->
                    <td >{{ produto.id }}</td> <!--celulas do registro-->
                    <td>{{ produto.nome }}</td>
                    <td>R$ {{ produto.preco|intcomma }}</td> <!--intcommma formata os numeros conforme a idioma-->
                    <td>
                        <a class="btn btn-warning" href="{% url 'upd_produto' produto.pk %}">Editar</a> <!-- aqui -->
                        <a class="btn btn-danger" href="#">Deletar</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
```

## Delete

- Em Aula_5_CRUD_Class_Based_View\crudcbv\core\views.py:

```python
from django.db import models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Produto
from .forms import ProdutoModelForm


class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all() # qual consulta quer fazer no banco de dados.
    context_object_name = 'produtos'
    
class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('index')

class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto_del.html'
    success_url = reverse_lazy('index')

```

Em Aula_5_CRUD_Class_Based_View\crudcbv\crudcbv\urls.py:

```python
from django.urls import path

from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),    
    path('add/', CreateProdutoView.as_view(), name='add_produto'),
    path('<int:pk>/update', UpdateProdutoView.as_view(), name='upd_produto'),
    path('<int:pk>/delete', DeleteProdutoView.as_view(), name='del_produto')
]
```

Em Aula_5_CRUD_Class_Based_View\crudcbv\core\templates\produto_del.html:

```html
{% extends 'base.html' %}
{% load bootstrap4 %}

{% block content %}
    <form method="post">
        {% csrf_token %}
        <p>Tem certeza que deseja deletar o produto "{{ object }}"</p>
        {% buttons %}
            <button type="submit" class="btn btn-danger">Confirmar</button>
            <button type="button" class="btn btn-warning">
                <a href="{% url 'index' %}">Cancelar</a>
            </button>
        {% endbuttons %}
    </form>
{% endblock %}

```

Em Aula_5_CRUD_Class_Based_View\crudcbv\core\templates\index.html:

```html
{% extends "base.html" %}
{% load humanize %}

{% block content %}
    <div class ="row">
        <h1>Produto</h1>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Nome</th>
                    <th scope="col">Preço</th>
                    <th scope="col">Ação</th>
                </tr>
            </thead>
            <tbody>
                {% for produto in produtos %}
                <tr> <!--Linha-->
                    <td >{{ produto.id }}</td> <!--celulas do registro-->
                    <td>{{ produto.nome }}</td>
                    <td>R$ {{ produto.preco|intcomma }}</td> <!--intcommma formata os numeros conforme a idioma-->
                    <td>
                        <a class="btn btn-warning" href="{% url 'upd_produto' produto.pk %}">Editar</a> <!-- aqui -->
                        <a class="btn btn-danger" href="{% url 'del_produto' produto.pk %}">Deletar</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
{% endblock %}
```

Somente o model foi utilizado para criar as Class Based Views, não sendo necessario o 
form.

O formulário é utilizado para salvar dados no banco de dados
