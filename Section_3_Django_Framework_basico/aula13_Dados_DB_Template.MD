# Apresentando dados do BD no template.

Na view (Projetos\core\views.py):

```python
from django.shortcuts import render

from .models import Produto

def index(request):
    produtos = Produto.objects.all()

    context ={
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa!!',
        'produtos': produtos,
    }
    return render(request, 'index.html', context=context)

```

No template (Projetos\core\templates\index.html):

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Django 1 - Index</title>
    </head>
    <body>
        <h1>Index</h1>
        <h2>{{ curso }}</h2>
        <h2>{{ outro }}</h2>

        <table>
            <thead>
                <tr>
                    <th>Produto</th>
                    <th>Preço</th>
                </tr>
            </thead>
            <tbody>
            {% for produto in produtos %}
                <tr>
                    <td><a href="{% url 'produto' produto.id %} ">{{ produto.nome }} </a></td> 
                    <!-- esse 'produto' está referenciando pela variavel nome em urls e pelo nome da função em views/urls-->
                    <td>{{ produto.preco }} </td>
                </tr>
            {% endfor %}
            </tbody>
        </table>

    </body>
</html>
```

No urls.py (Projetos\core\urls.py):

```python

from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('' , index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto')
]
```

Na view (Projetos\core\views.py):

```python

def produto(request,pk):
    prod = Produto.objects.get(id=pk)

    contexto = {
        'produto' : prod
    }
    return render(request, 'produto.html', context=contexto)

```

Criar a página produtos.html na pasta templates (Projetos\core\templates):

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>{{ produto.nome }} </title>
    </head>
    <body>
        <h1>Produto</h1>

        <table>
            <thead>
                <tr>
                    <th>Produto</th>
                    <th>Preço</th>
                    <th>estoque</th>
                </tr>
            </thead>
            <tbody>
                    <td><a href="{% url 'index' %} ">{{ produto.nome }} </a></td>
                    <td>{{ produto.preco }} </td>
                    <td>{{ produto.estoque }} </td>
                </tr>
            </tbody>
        </table>

    </body>
</html>


```