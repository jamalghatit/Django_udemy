# Publicando na internet seu segundo projeto Django

/django2/settings.py:

```python
DEBUG = False # Colocar DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhitenoiseMiddleware', # descomentar a linha do whitenoise(arquivos estáticos)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #Comentar essa linha

"""
O heroku não da suporte gratuito ao mysql, portanto comentar o dicionario DATABASES.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django2',
        'USER': 'geek',
        'PASSWORD':'univesity',
        'HOST' : 'localhost',
        'PORT' : '3306',
    }
}
"""

import dj_database_url # importar no começo do arquivo essa biblioteca

# Usando PostgreSQL com Heroku
DATABASES = {
    'default': dj_database_url.config()
}


```

Instalar esses pacotes devido ao heroku não da suporte gratuito ao Mysql, somente
ao SQlite e o postgres:

```bash
pip install dj_database_url psycopg2-binary

pip freeze > requirements.txt
```

Copiar a pasta do projeto, iniciar o git:

```bash

\$ git init

$ git add .

$ git commit -m 'projeto finalizado'

$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/55a24444-5c55-46eb-ba15-4746d846095d?requestor=SFMyNTY.g2gDbQAAAA0xODcuMzQuODAuMTA1bgYAK_OAjngBYgABUYA.pqE8rHBt4C0wGRqNaxtL07ZPG7omLzPxtZ3NGVYVs1M
heroku: Waiting for login...
Logging in... done
Logged in as email@gmail.com

$ python -V
Python 3.9.2
(venv)

```
Criar um arquivo chamado runtime.txt:

```text
python-3.9.2

```

Criar o arquivo ProcFile:

```text
web: gunicorn django2.wsgi --log-file -
```

Criar uma aplicação no heroku:

```bash

$ heroku create django3-jg --buildpack heroku/python

Creating django3-jg... done
Setting buildpack to heroku/python... done
https://django3-jg.herokuapp.com/ | https://git.heroku.com/django3-jg.git

$ git push heroku master

Enumerating objects: 7237, done.
Counting objects: 100% (7237/7237), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4231/4231), done.
Writing objects: 100% (7237/7237), 11.21 MiB | 5.82 MiB/s, done.
Total 7237 (delta 1916), reused 7225 (delta 1912), pack-reused 0
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Building on the Heroku-20 stack
remote: -----> Using buildpack: heroku/python
remote: -----> Python app detected
remote: -----> Installing python-3.9.2
remote: -----> Installing pip 20.1.1, setuptools 47.1.1 and wheel 0.34.2
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting asgiref==3.3.1
remote:          Downloading asgiref-3.3.1-py3-none-any.whl (19 kB)
remote:        Collecting beautifulsoup4==4.9.3
remote:          Downloading beautifulsoup4-4.9.3-py3-none-any.whl (115 kB)
remote:        Collecting dj-database-url==0.5.0
remote:          Downloading dj_database_url-0.5.0-py2.py3-none-any.whl (5.5 kB)
remote:        Collecting Django==3.1.7
remote:          Downloading Django-3.1.7-py3-none-any.whl (7.8 MB)
remote:        Collecting django-bootstrap4==2.3.1
remote:          Downloading django_bootstrap4-2.3.1-py3-none-any.whl (24 kB)
remote:        Collecting django-stdimage==5.2.0
remote:          Downloading django_stdimage-5.2.0-py2.py3-none-any.whl (14 kB)
remote:        Collecting gunicorn==20.0.4
remote:          Downloading gunicorn-20.0.4-py2.py3-none-any.whl (77 kB)
remote:        Collecting mysql-connector-python==8.0.23
remote:          Downloading mysql_connector_python-8.0.23-py2.py3-none-any.whl (379 kB)
remote:        Collecting mysqlclient==2.0.3
remote:          Downloading mysqlclient-2.0.3.tar.gz (88 kB)
remote:        Collecting Pillow==8.1.2
remote:          Downloading Pillow-8.1.2-cp39-cp39-manylinux1_x86_64.whl (2.2 MB)
remote:        Collecting progressbar2==3.53.1
remote:          Downloading progressbar2-3.53.1-py2.py3-none-any.whl (25 kB)
remote:        Collecting protobuf==3.15.6
remote:          Downloading protobuf-3.15.6-cp39-cp39-manylinux1_x86_64.whl (1.0 MB)
remote:        Collecting psycopg2-binary==2.8.6
remote:          Downloading psycopg2_binary-2.8.6-cp39-cp39-manylinux1_x86_64.whl (3.0 MB)
remote:        Collecting PyMySQL==1.0.2
remote:          Downloading PyMySQL-1.0.2-py3-none-any.whl (43 kB)
remote:        Collecting python-utils==2.5.6
remote:          Downloading python_utils-2.5.6-py2.py3-none-any.whl (12 kB)
remote:        Collecting pytz==2021.1
remote:          Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
remote:        Collecting six==1.15.0
remote:          Downloading six-1.15.0-py2.py3-none-any.whl (10 kB)
remote:        Collecting soupsieve==2.2
remote:          Downloading soupsieve-2.2-py3-none-any.whl (33 kB)
remote:        Collecting sqlparse==0.4.1
remote:          Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
remote:        Collecting whitenoise==5.2.0
remote:          Downloading whitenoise-5.2.0-py2.py3-none-any.whl (19 kB)
remote:        Building wheels for collected packages: mysqlclient
remote:          Building wheel for mysqlclient (setup.py): started
remote:          Building wheel for mysqlclient (setup.py): finished with status 'done'
remote:          Created wheel for mysqlclient: filename=mysqlclient-2.0.3-cp39-cp39-linux_x86_64.whl size=111132 sha256=02656ac889820ab04f19c2a7748dc22c0b44169c5247a706c363cb3fe5e59113
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-_9oaq5xy/wheels/43/55/d9/a2243d4b624c18c5cba30bf88e0521147498368068cb302532
remote:        Successfully built mysqlclient
remote:        Installing collected packages: asgiref, soupsieve, beautifulsoup4, dj-database-url, sqlparse, pytz, Django, django-bootstrap4, six, python-utils, progressbar2, Pillow, django-stdimage, gunicorn, protobuf, mysql-connector-python, mysqlclient, psycopg2-binary, PyMySQL, whitenoise
remote:        Successfully installed Django-3.1.7 Pillow-8.1.2 PyMySQL-1.0.2 asgiref-3.3.1 beautifulsoup4-4.9.3 dj-database-url-0.5.0 django-bootstrap4-2.3.1 django-stdimage-5.2.0 gunicorn-20.0.4 mysql-connector-python-8.0.23 mysqlclient-2.0.3 progressbar2-3.53.1 protobuf-3.15.6 psycopg2-binary-2.8.6 python-utils-2.5.6 pytz-2021.1 six-1.15.0 soupsieve-2.2 sqlparse-0.4.1 whitenoise-5.2.0
remote: -----> $ python manage.py collectstatic --noinput
remote:        133 static files copied to '/tmp/build_fffec27d/staticfiles'.
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> (none)
remote:
remote: -----> Compressing...
remote:        Done: 77.8M
remote: -----> Launching...
remote:        Released v5
remote:        https://django3-jg.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/django3-jg.git
 * [new branch]      master -> master


$ heroku run python manage.py migrate

Running python manage.py migrate on django3-jg... starting, run.6584 (Free)
Running python manage.py migrate on django3-jg... connecting, run.6584 (Free)Running python manage.py migrate on django3-jg... up, run.6584 (Free)
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying core.0001_initial... OK
  Applying sessions.0001_initial... OK

$ heroku run python manage.py createsuperuser

Running python manage.py createsuperuser on django3-jg... starting, run.7660 (Free)
Running python manage.py createsuperuser on django3-jg... connecting, run.7660 (Free)Running python manage.py createsuperuser on django3-jg... up, run.7660 (Free)
Usuário (leave blank to use 'u31709'): geek
geek
Endereço de email:

Password: university

Password (again): university

```

modificar index.html

```html

{% load bootstrap4 %}
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <title>Index</title>
    <meta charset="utf-8">
    {% bootstrap_css %}
    <link rel="stylesheet" href='{% static "css/styles.css" %}'>
  </head>
  <body>
    <div class='container'>
      <h1>Produtos</h1>
        {% if produtos %}
      <table class='table table-dark'>
        <!-- https://getbootstrap.com/docs/4.1/content/tables/ -->
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Produto</th>
            <th scope="col">Preço</th>
            <th scope="col">Estoque</th>
          </tr>
        </thead>
        <tbody>
          {% for produto in produtos %}
            <tr>
              <td scope="row">{{ produto.id }}</td>
              <td scope="row"><a href="#modal{{produto.id}}" data-toggle='modal'>{{ produto.nome }}</a></td>
              <td scope="row">{{ produto.preco }}</td>
              <td scope="row">{{ produto.estoque }}</td>
            </tr>
            <!--https://getbootstrap.com/docs/4.1/components/modal/#vertically-centered-->
            <div class='modal fade bd-example-modal-lg show' id='modal{{produto.id}}' role='dialog'>
              <div class='modal-dialog'>
                  <div class='modal-content'>
                    <div class="modal-header">
                      <button type='button' class='close' data-dismiss='modal'>
                        <span aria-hidden='true'>&times;</span>
                      </button>
                    </div>
                    <div class='modal-body' id='dynamic.content'>
                      <img src='{{ produto.imagem.url }}' class='img-fluid' alt='{{ produto.nome }}'/>
                  </div>
                </div>
              </div>
            </div>
          {% endfor %}
        </tbody>
      </table>
      {% else %}
          <h2>Ainda não existem produtos cadastrados.</h2>
      {% endif %}
    </div>
  {% bootstrap_javascript jquery='full' %}
</body>
</html>

```

O whitenoise apresenta os arquivos estaticos e não os arquivos'medias'
que são upload pelos usuários, para mostrar instale:

```bash

\$ pip install dj-static

$ pip uninstall whitenoise
```

Settings.py:

```python

# Remover o whitenoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


```

django2/wsgi.py:

```python

from dj_static import Cling, MediaCling

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django2.settings')

application = Cling(MediaCling(get_wsgi_application()))

```

O whitenoise fornece apenas os arquivos estáticos

Cling vai apresentar os arquivos estaticos como css, imgs, etc.
MediaCling vai apresentar os arquivos de upload do usuário.

Para resetar o DB:

```bash

$ heroku pg:reset DATABASE_URL

```

Para recriar as tabelas:

```bash

heroku run python manage.py migrate

heroku run python manage.py createsuperuser

```

## dj-database-url

This simple Django utility allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

The dj_database_url.config method returns a Django database connection dictionary, populated with all the data specified in your URL. There is also a conn_max_age argument to easily enable Django’s connection pool.

## psycopg2-binary

Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety (several threads can share the same connection). It was designed for heavily multi-threaded applications that create and destroy lots of cursors and make a large number of concurrent “INSERT”s or “UPDATE”s.

## dj-static

This is a simple Django middleware utility that allows you to properly serve static assets from production with a WSGI server like Gunicorn.

Django doesn’t recommend the production use of its static file server for a number of reasons. There exists, however, a lovely WSGI application aptly named Static.

It is suitable for the production use of static file serving, unlike Django.