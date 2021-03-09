# Models

Quem tem o arquivo models é a aplicação.
O Django trabalha no padrão MTV (Model, Template, View)

O model é um modelo de dados. Com base nas classes definidas no models,
o django cria tabelas no banco de dados.

Projetos\core\models.py:

```python

from django.db import models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')


```

Depois de definir os modelos, verificar se voce colocou no arquivo
settings.py a sua aplicação em INSTALLED_APPS:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
```

Depois de criar o modelo em models.py, realizar a migration por meio
do comando 
` python manage.py makemigrations`

Esse comando vai pegar todas as aplicações do projeto, todos os modelos, 
e criar um arquivo de migration na pasta migrations dentro da pasta do projeto.

```bash
$ python manage.py makemigrations
Migrations for 'core':
  core\migrations\0001_initial.py
    - Create model Produto
```

core\migrations\0001_initial.py:

```python
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade em Estoque')),
            ],
        ),
    ]

```

A partir dessa migration, é criado a tabela de banco de dados.

Para saber qual banco de dados ele cria, há essa definição no arquivo settings.py:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Por padrão, é criado sqlite3, que é o que ja vem por padrão no python.

Dentro da pasta migrations, é arquivado toda migração realizada, tendo assim o seu
historico. Caso precise desfazer alguma modificação, é possível escolher de qual ponto
se deseja voltar.

Depois de criar a migrations, é necessário aplicá-la:
`python manage.py migrate`

Outro modelo em models.py:

```python

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    nome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

```

Realizar as migrações:

```bash
$ python manage.py makemigrations
Migrations for 'core':
  core\migrations\0002_cliente.py
    - Create model Cliente
```

```python

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
            ],
        ),
    ]

```

Aplicar as migrações:

```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  Applying core.0002_cliente... OK
```
