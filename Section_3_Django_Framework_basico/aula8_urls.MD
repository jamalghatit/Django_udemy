# Urls.py

As rotas, por padrão, são definidas no projeto.
Já as views são definidas na aplicação

urls.py do projeto:

```python 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]
```

urls.py da aplicação core:

```python
from django.urls import path
from .views import index, contato

urlpatterns = [
    path('', index)
    path('contato', contato)
]
```

Não é ideal criar as rotas na urls.py do projeto, mas sim criar
para cada projeto.