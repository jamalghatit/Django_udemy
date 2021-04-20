# Trabalhando com Class Based Views

Em fusion/core/views.py:

```python

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

```

Em fusion/core/urls.py:

```python

from django.urls import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
```
