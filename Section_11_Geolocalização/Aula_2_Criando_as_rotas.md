# Criando as rotas

Em Section_11_Geolocalização\geo\core\urls.py:

```python
from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
```

Em Section_11_Geolocalização\geo\geo\urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]

```