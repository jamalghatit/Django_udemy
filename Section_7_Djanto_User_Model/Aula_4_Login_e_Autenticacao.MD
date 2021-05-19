# Login e autenticação

Em django_user_model_customizado\django_user_model_customizado\urls.py:
O que tiver com '#' é a linha que foi adicionada

```python
from django.contrib import admin
from django.urls import path,
from django.urls import include #
from django.views.generic.base import TemplateView #

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),#
    path('', TemplateView.as_view(Template_name='index.html'), name='index')#
]
```

No bash:

```python
>>> from django.urls import get_resolver

>>> from pprint import pprint
>>> help(pprint)
Help on function pprint in module pprint:

pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True)
    Pretty-print a Python object to a stream [default is sys.stdout].

>>> pprint(get_resolver().url_patterns[0].url_patterns)

[<URLPattern '' [name='index']>,
 <URLPattern 'login/' [name='login']>,
 <URLPattern 'logout/' [name='logout']>,
 <URLPattern 'password_change/' [name='password_change']>,
 <URLPattern 'password_change/done/' [name='password_change_done']>,
 <URLPattern 'autocomplete/' [name='autocomplete']>,
 <URLPattern 'jsi18n/' [name='jsi18n']>,
 <URLPattern 'r/<int:content_type_id>/<path:object_id>/' [name='view_on_site']>,
 <URLResolver <URLPattern list> (None:None) 'auth/group/'>,
 <URLResolver <URLPattern list> (None:None) 'usuarios/customusuario/'>,
 <URLPattern '^(?P<app_label>auth|usuarios)/$' [name='app_list']>,
 <URLPattern '(?P<url>.*)$'>]

```

Em django_user_model_customizado\templates\base.html:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Geek University</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit-no">
    <link rel='icon' href='http://www.geekuniversity.com.br/static/images/favicon.4fcb819d32bf.ico'>
    <link href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' rel='stylesheet' id="bootstrap-css">
    <link href='https://getbootstrap.com/docs/4.0/examples/sign-in/signin.css' rel='stylesheet'>
</head>

<body class='text-center'>
    {% block content %} {% endblock %}

    <script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js'></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</body>

</html>

```

Em django_user_model_customizado\templates\index.html:

```html
{% extends 'base.html' %}

{% block content %}
    <div class="container">
        <h1>Geek University</h1>
        {% if user.is_anonymous %}
            <a class='btn btn-primary' href="{% url 'login' %}">Login</a>
        {% else %}
            <div class='alert alert-primary' role='alert' >
                Seja bem-vindo(a) {{ user.get_full_name }}!
            </div>
            <a class='btn btn-primary' href="{% url 'logout' %}"> Logout </a>
        {% endif %}
    </div>
{% endblock %}
```

Criar uma pasta dentro de Template com o nome de registration (é a pasta 
na qual o django procura sobre autenticação) e criar o arquivo login.html

Em django_user_model_customizado\templates\registration\login.html:

```html
{% extends "base.html" %}
{% block content %}
    <form class='form-signin' method='post' autocomplete='off'>
        {% csrf_token %}
        <img class='mb-4' scr='http://www.geekuniversity.com.br/static/images/favicon.4fcb819d32bf.ico' alt='' width='72' height='72'>
        <h1 class='h3 mb-3 font-weight-normal'>Informe seus dados</h1>

        <label for='username' class='sr-only'>E-mail</label>
        <input type='email' id ='username' name='username' class='form-control' placeholder='Informe seu e-mail' required autofocus>

        <label for='password' class='sr-only'>Senha</label>
        <input type='password' id ='password' name='password' class='form-control' placeholder='Informe sua senha' required>
        <button class='btn btn-lg btn-primary btn-block' type='submit'>Acessar</button>
        <p class='mt-5 mb-3 text-muted'>&copy; {% now 'Y' %}</p>

    </form>
{% endblock %}

```

Em django_user_model_customizado\settings.py:

```python 

LOGIN_REDIRECT_URL = 'index' 
LOGOUT_REDIRECT_URL = 'index'
```