# Publicando na internet seu primeiro projeto Django

ir em setting.py e mudar para DEBUG=False,
e ALLOWED_HOST para ['*']

## ALLOWED_HOST

A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations.

Instalar as bibliotecas whitenoise e gunicorn
`pip install whitenoise gunicorn`

whitenoise -> The WhiteNoise project provides a better way to serve static files for Django projects.

gunicorn -> Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX.

Configurar adicionar a seguinte linha no arquivo settings.py:

```python

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  # Certifique-se que o WhiteNoise seja adicionado acima de todos os middlewares do Django, exceto o de security. 
  # ...
]
```

Criar um arquivo na raiz do projeto chamado .gitignore (Projetos):

> arquivos começados com ~ (til) são arquivos temporários.
> .pyc -> arquivos complilados python

```text
__pycache__

*.*~

*.pyc

.idea
```

Iniciar o git na pasta do projeto (Projetos):

```bash
$ git init #  Create an empty Git repository or reinitialize an existing one
Initialized empty Git repository in C:/Users/jamal_ghatit/Documents/GitHub/Django_udemy/Section_3_Django_Framework_basico/Projetos/.git/
(venv)

$ git status # Show the working tree status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        core/
        db.sqlite3
        django1/
        manage.py
        staticfiles/

nothing added to commit but untracked files present (use "git add" to track)

$ git commit -m 'Projeto finalizado' # Record changes to the repository

```

Acessar o site [Heroku.com](https://www.heroku.com/) e se cadastrar.

Fazer o download do CLI do heroku em [Heroku] (https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

Depois criar um arquivo na raiz do projeto chamado runtime.txt e  no arquivo, colocar a 
versão do python utilizada no projeto.

```txt
python-3.8.8

```

O heroku vai criar uma maquina virtual do zero, vai instalar todas as bibliotecas necessárias e vai instalar o mesmo python para não ter problemas e a versão ele vai buscar
no arquivo runtime.txt

Criar um arquivo na raiz do projeto chamado Procfile:

```txt
web: gunicorn django1.wsgi --log-file -

```

Fazer login no heroku e criar uma aplicação:

```bash
$ heroku login

heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/cli/browser/c393eb07-be2c-46f3-ac40-674c95e9e65c?requestor=SFMyNTY.g2gDbQAAAA0xOTEuMTkzLjUwLjUwbgYAAaAnLngBYgABUYA.FYabkD6IbgFCRKtNWc9ukzqXg6SryYeEXXRqG2Sr7xA
Logging in... done
Logged in as email@gmail.com

$ heroku create django1-jg --buildpack heroku/python

Creating ⬢ django1-jg... done
Setting buildpack to heroku/python... done
https://django1-jg.herokuapp.com/ | https://git.heroku.com/django1-jg.git

```

Depois disso, fazer o upload dos arquivos do git no heroku:

```bash

$ git push heroku master

Enumerating objects: 193, done.
Counting objects: 100% (193/193), done.
Delta compression using up to 12 threads
Compressing objects: 100% (183/183), done.
Writing objects: 100% (193/193), 646.67 KiB | 10.26 MiB/s, done.
Total 193 (delta 37), reused 0 (delta 0), pack-reused 0
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Building on the Heroku-20 stack
remote: -----> Python app detected
remote: -----> Installing python-3.8.8
remote: -----> Installing pip 20.1.1, setuptools 47.1.1 and wheel 0.34.2
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting Django==3.1.7
remote:          Downloading Django-3.1.7-py3-none-any.whl (7.8 MB)
remote:        Collecting gunicorn==20.0.4
remote:          Downloading gunicorn-20.0.4-py2.py3-none-any.whl (77 kB)
remote:        Collecting pytz==2021.1
remote:          Downloading pytz-2021.1-py2.py3-none-any.whl (510 kB)
remote:        Collecting sqlparse==0.4.1
remote:          Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
remote:        Collecting whitenoise==5.2.0
remote:          Downloading whitenoise-5.2.0-py2.py3-none-any.whl (19 kB)
remote:        Collecting asgiref<4,>=3.2.10
remote:          Downloading asgiref-3.3.1-py3-none-any.whl (19 kB)
remote:        Installing collected packages: asgiref, pytz, sqlparse, Django, gunicorn, whitenoise
remote:        Successfully installed Django-3.1.7 asgiref-3.3.1 gunicorn-20.0.4 pytz-2021.1 sqlparse-0.4.1 whitenoise-5.2.0
remote: -----> $ python manage.py collectstatic --noinput
remote:        132 static files copied to '/tmp/build_d783a22a/staticfiles', 3 unmodified.
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 57.5M
remote: -----> Launching...
remote:        Released v5
remote:        https://django1-jg.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/django1-jg.git
 * [new branch]      master -> master

```

Após realizar qualquer modificação no projeto, 
fazer o push para a master no heroku

```bash
$ git push heroku master

```

Para verificar o logs do heroku:

> $ heroku logs --tail