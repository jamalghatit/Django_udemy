#  Publicando na internet seu terceiro projeto Django

- criar o arquivo .gitignore

```
venv
*.*~
**/__pycache__
*.pyc
.vscode/settings.json
venv/
```

Em rojeto\fusion\wsgi.py:

```python

"""
WSGI config for fusion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fusion.settings')

application = Cling(MediaCling(get_wsgi_application()))

# dj_static é utilizado para apresentação de arquivos estáticos, 
# O Cling é para arquivos estáticos e o MediaCling para apresentação de 
# mídia, ou seja, arquivos de upload pelo usuário.

```

Instalar o app dj-database-url e add no requirements.txt:

```bash

pip install dj-database-url

pip freeze > requiments.txt

```

dj-database-url: Use Database URLs in your Django Application.


Em Projeto\fusion\settings.py:

```python
# importar o modulo dj_database_url

import dj_database_url

# Comentar o dicionario DATABASES.
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fusion',
        'USER': 'geek',
        'PASSWORD': 'university',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}"""

# esse dj_database_config vai ler as configurações do heroku e vai passar os dados
# que a gente precisa para ter acesso ao banco de dados.

DATABASES = {
    'default': dj_database_url.config()
}

# Comentar o EMAIL_BACKEND

"""
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""

# Adicionar a configuração para que quando o usuário deslogar, ele ir para
# a pagina inicial

LOGOUT_REDIRECT_URL = 'index'

```

Copiar a pasta projetos para outro local e criar um repositório local:

```bash

git init

# adicionar todos os arquivos.
git add.

# Comitar os arquivos
git commit -m 'projeto finalizado'

# fazer login na conta do heroku
heroku login
```

Criar um arquivo na raiz do projeto runtime.txt contendo a versão do python
para informar qual versão do python o heroku vai rodar.

```text
python-3.9.5
```

Criar um arquivo chamado Procfile:

```text
web: gunicorn fusion.wsgi --log-file -
```

Agora tem que criar a aplicação:

```bash
$ heroku create fusion-jag --buildpack heroku/python
Creating ⬢ fusion-jag... done
Setting buildpack to heroku/python... done
https://fusion-jag.herokuapp.com/ | https://git.heroku.com/fusion-jag.git
```

Colocar no setting.py o Debug = False

E depois publicar no heroku:

```bash
$ git push heroku master
Enumerating objects: 134, done.
Counting objects: 100% (134/134), done.
Delta compression using up to 12 threads
Compressing objects: 100% (129/129), done.
Writing objects: 100% (134/134), 3.18 MiB | 2.15 MiB/s, done.
Total 134 (delta 18), reused 0 (delta 0), pack-reused 0
remote: Git submodules detected, installing:
remote:
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Building on the Heroku-20 stack
remote: -----> Using buildpack: heroku/python
remote: -----> Python app detected
remote: -----> Using Python version specified in runtime.txt
remote: -----> Installing python-3.9.5
remote: -----> Installing pip 20.2.4, setuptools 47.1.1 and wheel 0.36.2
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting dj-database-url==0.5.0
remote:          Downloading dj_database_url-0.5.0-py2.py3-none-any.whl (5.5 kB)
remote:        Collecting dj-static==0.0.6
remote:          Downloading dj-static-0.0.6.tar.gz (3.4 kB)
remote:        Collecting Django==2.2.5
remote:          Downloading Django-2.2.5-py3-none-any.whl (7.5 MB)
remote:        Collecting django-adminlte2==0.4.1
remote:          Downloading django_adminlte2-0.4.1-py3-none-any.whl (4.5 MB)
remote:        Collecting django-stdimage==5.0.1
remote:          Downloading django_stdimage-5.0.1-py2.py3-none-any.whl (14 kB)
remote:        Collecting gunicorn==19.9.0
remote:          Downloading gunicorn-19.9.0-py2.py3-none-any.whl (112 kB)
remote:        Collecting Pillow==6.1.0
remote:          Downloading Pillow-6.1.0.tar.gz (33.8 MB)
remote:        Collecting progressbar2==3.43.1
remote:          Downloading progressbar2-3.43.1-py2.py3-none-any.whl (21 kB)
remote:        Collecting psycopg2-binary==2.8.3
remote:          Downloading psycopg2-binary-2.8.3.tar.gz (378 kB)
remote:        Collecting python-utils==2.3.0
remote:          Downloading python_utils-2.3.0-py2.py3-none-any.whl (12 kB)
remote:        Collecting pytz==2019.2
remote:          Downloading pytz-2019.2-py2.py3-none-any.whl (508 kB)
remote:        Collecting six==1.12.0
remote:          Downloading six-1.12.0-py2.py3-none-any.whl (10 kB)
remote:        Collecting sqlparse==0.3.0
remote:          Downloading sqlparse-0.3.0-py2.py3-none-any.whl (39 kB)
remote:        Collecting static3==0.7.0
remote:          Downloading static3-0.7.0.tar.gz (24 kB)
remote:        Building wheels for collected packages: dj-static, Pillow, psycopg2-binary, static3
remote:          Building wheel for dj-static (setup.py): started
remote:          Building wheel for dj-static (setup.py): finished with status 'done'
remote:          Created wheel for dj-static: filename=dj_static-0.0.6-py3-none-any.whl size=3053 sha256=6bd7c567e1bcf7b6c9cffb3618fc1c2a868531a348af373135adc2e13a893629
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-14iz32y3/wheels/b5/10/4a/83f0c20117a4580af66c382f5cd1c689e6a8818a042ffdedd3
remote:          Building wheel for Pillow (setup.py): started
remote:          Building wheel for Pillow (setup.py): finished with status 'done'
remote:          Created wheel for Pillow: filename=Pillow-6.1.0-cp39-cp39-linux_x86_64.whl size=1387934 sha256=57d4bc6b9347e3c3cf768e86f8b278da733f94164a70503053c2a0ba8aaa6889
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-14iz32y3/wheels/03/64/f4/5ca17eda7a165f340133f70d5054308dc827922d93e14ce1c7
remote:          Building wheel for psycopg2-binary (setup.py): started
remote:          Building wheel for psycopg2-binary (setup.py): finished with status 'done'
remote:          Created wheel for psycopg2-binary: filename=psycopg2_binary-2.8.3-cp39-cp39-linux_x86_64.whl size=517514 sha256=b4b6800611b71446af6f3d9c779eb7f5771be2eaf369566d6248fb6f499ec9cb
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-14iz32y3/wheels/e8/d8/d8/a7c3fdcf887ec3c60f24c2770327261614baf96a5e06d2ebd5
remote:          Building wheel for static3 (setup.py): started
remote:          Building wheel for static3 (setup.py): finished with status 'done'
remote:          Created wheel for static3: filename=static3-0.7.0-py3-none-any.whl size=18605 sha256=af0bf2bf9d4e3bc795a54206940f2dc3080042804634f622be72b57a1bb4c0f8
remote:          Stored in directory: /tmp/pip-ephem-wheel-cache-14iz32y3/wheels/67/88/26/362b5f8314043c6241ed324b9f76ddf48328b775923b39590a
remote:        Successfully built dj-static Pillow psycopg2-binary static3
remote:        Installing collected packages: dj-database-url, static3, dj-static, pytz, sqlparse, Django, django-adminlte2, six, python-utils, progressbar2, Pillow, django-stdimage, gunicorn, psycopg2-binary
remote:        Successfully installed Django-2.2.5 Pillow-6.1.0 dj-database-url-0.5.0 dj-static-0.0.6 django-adminlte2-0.4.1 django-stdimage-5.0.1 gunicorn-19.9.0 progressbar2-3.43.1 psycopg2-binary-2.8.3 python-utils-2.3.0 pytz-2019.2 six-1.12.0 sqlparse-0.3.0 static3-0.7.0
remote: -----> $ python manage.py collectstatic --noinput
remote:        178 static files copied to '/tmp/build_1497177c/staticfiles'.
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 73.9M
remote: -----> Launching...
remote:        Released v5
remote:        https://fusion-jag.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/fusion-jag.git
 * [new branch]      master -> master

```

Criar as tabelas no DB no heroku:

```bash

$ heroku run python manage.py migrate
Running python manage.py migrate on ⬢ fusion-jag... up, run.8860 (Free)
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
  Applying core.0001_initial... OK
  Applying core.0002_alter_team_image... OK
  Applying sessions.0001_initial... OK

```

criar superusuario:

```bash

heroku run python manage.py createsuperuser
user: jamaljag
pass: portugal@2040
```

Adicionar os serviços e as equipes no admin.

Para adicionar uma nova interface ao django admin, instalar o
django-adminlte2 e adicioná-lo no settings.py

```python

INSTALLED_APPS = [

    'django_adminlte', #
    'django_adminlte_theme', #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

```

O projeto está em https://fusion-jag.herokuapp.com/

Para visualizar as modificações feitas para add no heroku,
visualizar o código:

```bash

$ heroku login
$ heroku git:clone -a fusion-jag
$ cd fusion-jag

```