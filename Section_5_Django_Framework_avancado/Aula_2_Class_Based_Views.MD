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

Temos 4 categorias principais:
    - Base Generic Views
      - django.views.generic.View
      - django.views.generic.TemplateView
      - django.views.generic.RedirectView
    - List Generic View
      - django.views.generic.DetailView
    - Edit Generic views
      - django.views.generic.FormView
      - django.views.generic.Createview
      - django.views.generic.UpdateView
      - django.views.generic.DeleteView
  
## Uso da Class Based Views

Django Function Based View:

```python

from django. shortcuts import render

def index(request):
    return render(request, 'index.html')

```

Django Class Based View

```python

from django.views.generic import TemplateView

class indexView(TemplateView):
    template_name = 'index.html'
```

Os códigos acima funcionam de forma idêntica.

Exemplos:

Django Function Based View

```python
def index(request):
    context = {
        'produtos' : Produto.objects.all()
    }
    return render(request, 'index.html', context)
```

Django Class Based View

```python
from django.views.generic import View
from django.shortcuts import render

from .models import Produto

class IndexView(View):

    def get(self, request):
        context = {
            'produto' = Produto.objects.all()
        }
        return render(request, 'index.html', context)

```

Os códigos acima funcionam de forma idêntica.

Django Function Based View

```python
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Produto
from .forms import ProdutoForm

def produto(request):
    form = ProdutoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            form = ProdutoForm() # instancia novamente o classe, ou seja, zera o formulário.
            return reverse_lazy('produto') # retorna a pagina produto.
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)
```

Django Class Based View

```python
from django.views.generic import CreateView
from django.shortcuts import render

from .models import Produto
from .forms import ProdutoForm

class ProdutoView(CreateView):
    model = Produto
    form_class = ProdutoForm
    success_rul = reverse_lazy('produto')

```

Os códigos acima funcionam de forma idêntica.

## O lado sombrio das Class Based View

- É muito fácil você perder o caminho da origem dos seus métodos.
- Você pode poluir seu código com os diversos imports.
- O fluxo de controle é totalmente escondido.
- A ordem de execução dos métodos podem não serem obvias para ninguém.
- mais difícil de debugar.
- Para entender o que está acontecendo, você poderá precisar ler a documentação.

Lembre-se do Zen do Python:

'Explicit is better than implicit'

## Dicas finais

- Mantenha suas views simples.
- Não repita código nas suas views.
- Mantenha seus mixins simples.

Lembre-se do Zen do Python:

'Explicit is better than implicit'
