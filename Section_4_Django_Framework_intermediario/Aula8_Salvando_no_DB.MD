# Salvando dados no banco de dados

Não é ideal ter os arquivos que foram feitos upload estar na pasta produtos.

settings.py:

```python 

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')


```

django2/url.py:

```python 

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import staticc
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

core/views.py:

```python

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto salvo com sucesso')
            form = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar produto')
    else:
        form = ProdutoModelForm()

    context = {
        'form':form
    }
    return render(request, 'produto.html', context=context)

```
