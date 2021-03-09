# Templates

Depois de indicar no arquivo settings onde será localizado
o arquivo de templates:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # <-- AQUI
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
```

Criar as views:

```python
from django.shortcuts import render

def index(request):
    context = {
        'curso':'programação web com django framework,
        'outro':'Django é massa!!', 
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')
```

Criar rotas para as views:

```python
from django.urls import path
from .views import index, contato

urlpatterns = [
    path('' , index),
    path('contato', contato),
]
```
