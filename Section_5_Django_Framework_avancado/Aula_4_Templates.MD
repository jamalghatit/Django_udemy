# Definindo os Templates

Colar a pagina html de algum template (nesse projeto foi o fusion) na pasta templates /projeto/core/templates:

- Antes do cabeçalho do HTML, colocar isso caso vá carregar arquivos da pasta static : `{% load static %}` 

```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">

{% load static %}
```

Depois apontar para o local correto dos arquivos css,js,img, etc :

```html
 <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}" >
    <!-- Icon -->
    <link rel="stylesheet" href="{% static 'fonts/line-icons.css' %}">
    <!-- Owl carousel -->
    <link rel="stylesheet" href="{% static 'css/owl.carousel.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/owl.theme.css' %}">

    <!-- Animate -->
    <link rel="stylesheet" href="{% static 'css/animate.css' %}">
    <!-- Main Style -->
    <link rel="stylesheet" href="{% static 'css/main.css' %}">
    <!-- Responsive Style -->
    <link rel="stylesheet" href="{% static 'css/responsive.css' %}">
```

## Herança de template

- Criar uma pagina em branco chamada base.html
- Copiar todo o código do index.html e colar no base.html e colocar todo o conteúdo da pagina entre
`{% block content %} blablabla conteudo bla bla bla {% endblock %}`

- Apagar o conteúdo entre esses blocos:
`{% block content %}  {% endblock %}`

- Vai no index.html e apaga o cabeçalho e o footer, deixando apenas o conteúdo, ou seja, o conteúdo que não estão no base.html.

- Colocar entre o conteúdo da pagina index.html: `{% block content %}  {% endblock %}` e na primeira linha: 
`{% extends 'base.html' %}`

- Na pagina Base.html, arquivos que referenciam o index.html, colocar  ` <a href="{% url 'index' %}" `

- Criar uma pagina chamada hero.html com `{% load static %}` e copia o código do 'Hero Area' desde o 'start' até o 'End' da pagina index.html. Na pagina index.html, colocar no lugar do código copiado `{% include hero.html%}`

- Criar uma pagina chamada services.html com `{% load static %}` e copia o código do 'Service Section' desde o 'start' até o 'End' da pagina index.html.  Na pagina index.html, colocar no lugar do código copiado `{% include services.html %}`

- E fazer para todas as seções da pagina index.html...

```html

{% extends 'base.html' %}
{% load static %}
{% block content %}
     <!-- Hero Area Start -->
      {% include 'hero.html' %}
    <!-- Hero Area End -->

    <!-- Services Section Start -->
      {% include 'services.html' %}
    <!-- Services Section End -->

    <!-- About Section start -->
      {% include 'about.html' %}
    <!-- About Section End -->

    <!-- Features Section Start -->
      {% include 'features.html' %}
    <!-- Features Section End -->

    <!-- Team Section Start -->
      {% include 'team.html' %}
    <!-- Team Section End -->

    <!-- Pricing section Start -->
      {% include 'pricing.html' %}
    <!-- Pricing Table Section End -->

    <!-- Testimonial Section Start -->
      {% include 'testimonials.html' %}
    <!-- Testimonial Section End -->

    <!-- Call To Action Section Start -->
    {% include 'call.html' %}
    <!-- Call To Action Section Start -->

    <!-- Contact Section Start -->
    {% include 'contact.html' %}
    <!-- Contact Section End -->

    <!-- Footer Section Start -->
    {% include 'footer.html'%}
    <!-- Footer Section End -->
{% endblock %}

```

Em core/views.py:

```python
class TesteView(TemplateView):
    template_name = 'teste.html'
```

Em core/urls:

```python
from django.urls import path
from .views import IndexView, TesteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste/', TesteView.as_view(), name='teste')

]
```

Criar um template chamado teste.html:

```python
{% extends 'base.html' %}

{% block content %}
    <!-- Hero Area Start -->
    {% include 'hero.html' %}
    <!-- Hero Area End -->
    <br>
    <h1 align='center'>Teste :D</h1>
{% endblock %}

```

Criar as paginas 404.html e 500.html em templates, herdando de base.html `{% extends 'base.html' %}`

Depois ir em settings.py e colocar o debug como false para verificar que para se ter paginas de erros personalizadas
como 404 e 500, basta colocar na pasta templates, a pagina 404.html e 500.html, por exemplo. Isso foi uma atualização 
realizada no django.

