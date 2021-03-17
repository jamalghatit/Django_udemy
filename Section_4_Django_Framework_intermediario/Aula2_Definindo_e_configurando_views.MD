#  Definindo e configurando as views

Abrir o arquivo /core/views.py:

```python

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def produto(request):
    return render(request, 'produto.html')

```

Criar a pasta template e as paginas html.
Depois criar a pasta static para arquivos estaticos, e dentro
as pastas css, images, js.