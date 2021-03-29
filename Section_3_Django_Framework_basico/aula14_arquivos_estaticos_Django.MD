# Arquivos estáticos no Django: CSS, JavaScript e Imagens

O django utiliza o conceito de aplicações plugáveis, ou seja, poderiamos ter
varias aplicações.

Projetos\django1\settings.py:

```python

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True = modo desenvolvimento
# DEBUG = FALSE = modo produção
DEBUG = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/' # usado durante o desenvolvimento
STATIC_ROOT = path.join(BASE_DIR, 'staticfiles') # usado durante a produção.


```

O Django espera que cada aplicação tenha um diretório chamado
static e que lá contenha os arquivos estáticos.

Criar a estrutura de diretório padrão. Dentro do diretório
static, criar os diretórios css, imagens e js.

Quando o DEBUG=TRUE, o Django utiliza o STATIC_URL,
Quando o DEBUG=False, ou seja, modo produção, ele utiliza
o staticfiles

Criação de arquivo css (Projetos\core\static\css):

```css
body{
    background-color: bisque;
    color: darkblue;
}

a {
    text-decoration: none;
    color: black;
}
```

Criação de arquivo javascript (Projetos\core\static\js):

```javascript

function teste(){
    alert('funciona mesmo!!!');
}
```

Modificar a pagina html (Projetos\core\templates\index.html):

```html

{% load static %} <!-- Toda página que irá carregar arquivos estáticos,
tem que iniciar com isso.-->
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Django 1 - Index</title>
        <link rel="stylesheet" href="{% static 'css/estilos.css' %}"> <!--indicação de uso de css-->
    </head>
    <body>
        <h1>Index</h1>

        <img src='{% static "images/django.png" %}'>

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
                    <td><a href="{% url 'produto' produto.id %} ">{{ produto.nome }} 
                    </a></td>
                    <!-- esse 'produto' está referenciando pela variavel nome em urls e pelo nome da função em views/urls-->
                    <td>{{ produto.preco }} </td>
                </tr>
            {% endfor %}
            </tbody>
        </table>

        <button onClick='teste();'>Clique me!</button>
        <script type='text/javascript' src='{% static "js/script.js" %}'> </script>
    </body>
</html>

```

Mudar o DEBUG para false. 
Quando o DEBUG está igual False, o django buscará os arquivos estáticos 
na pasta staticfiles e não mais na pasta static.

Para copiar os arquivos estáticos de static para staticfile:

```bash

$ python manage.py collectstatic

135 static files copied to 'C:\Users\jamal_ghatit\Documents\GitHub\Django_udemy\Section_3_Django_Framework_basico\Projetos\staticfiles'.
(venv) 

```

Por padrão, ele não consegue servir arquivos estaticos quando esta em modo de produção.
Há outra ferramenta para isso.

--------------

Tratar o erro de pagina não existente:

No arquivo **views.py** (Projetos\core\urls.py):

```python

def produto(request,pk):
    prod = Produto.objects.get(id=pk)

    contexto = {
        'produto' : prod
    }
    return render(request, 'produto.html', context=contexto)

```

Em **urls.py** (Projetos\django1\urls.py):

```python

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import  handler404, handler500

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

handler404 = views.error404
handler500 = views.error500
```

Em **views.py** (Projetos\core\views.py):

```python

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=500)


```

Criar pagina 404 templates (Projetos\core\templates):

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>404</title>
    </head>
    <body>
        <h1>Página não encontrada</h1>
        <h2>Erro 404</h2>
    </body>
</html>

```

Criar pagina 500 em templates (Projetos\core\templates):

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>500</title>
    </head>
    <body>
        <h1>Erro no processamento</h1>
        <h2>Erro 500</h2>
    </body>
</html>

```

No arquivo setting.py (Projetos\django1\settings.py):

```python
LOGOUT_REDIRECT_URL = 'index' # é o nome declarado na urls

```

urls.py (Projetos\core\urls.py):

```python
from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('' , index, name='index'),
    path('contato', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto') 
]

```