# Conhecendo as Class Based Views

## Function Based Views

- no arquivo urls.py:

```python

from .views import index

urlpatterns = [
    path('', index, name=index),
]

```

- Em views.py

```python

def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

```

Uma view Django nada mais é do que uma **função** que:

- Recebe uma requisição (request) HTTP como entrada;
- Transforma em uma resposta (response) HTTP;

Request --> Index () --> Response

## O que seria uma Class Based View

- Views Djangos baseadas em classes;
- Sendo que estas classes são executadas como funções;
- Usando um recurso chamados de **mixins** para adicionar funcionalidades;

```python

urlspatterns = [
    path('', IndexView.as_view(), name='Index'),
]

Class IndexView(View):

    def get(self, request):
        return render(request, 'index.html')


```

## Como funciona as Class Based Views

![class_based_views](/Section_5_Django_Framework_avancado/img/class_based.PNG)

## Mixins

Mixins nada mais são do que classes Python que proveem alguma funcionalidade para ser herdada por outras classes, mas não são instanciadas por si só.

```python

class MeuMixin(object):

    def meu_metodo(self):
        pass
    def meu_metodo2(self):
        pass

```

### Qual objetivo?

- Adicionar funcionalidade para classes;
- Melhorar a modularidade;

### Quando usar mixins?

Quando se quer reutilizar código/funcionalidades entre múltiplas classes

### Regra prática

- As classes view based providas pelo Django sempre são posicionadas à direta.
- Mixins sempre são posicionadas à esquerda da classe view base.
- Mixins sempre devem herdar de object do Python

```python

class TemplateView(TemplateResponseMixin, ContextMixin, View):
    pass

class ContextMixin(object):
    pass

``` 

## Class Based Views integradas do Django.
