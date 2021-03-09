# Views

> projeto/aplicação/views.py

Quem tem views são as aplicações ('Core') e não os projetos (django1)

Uma view é uma função python:

```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


```

Quando o navegador acessa o site, a view recebe uma requisição. Antes de chegar na
View, ela passa pela url.

Não é possível acessar essas páginas, pois primeiro é necessário criar rotas para
esses arquivos, que será efetuada em urls.py

As views são criadas nas aplicações e não no projeto.