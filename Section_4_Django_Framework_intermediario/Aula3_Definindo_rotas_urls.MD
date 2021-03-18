#  Definindo e configurando as rotas

Acione na rota no arquivo de rotas do projeto (projeto/django2/urls.py), 
o arquivo de rota da aplicação (projeto/core/urls.py):

projeto/django2/urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls'))
]

``` 

projeto/core/urls.py

```python

from django.urls import path

from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto,name='produto')
]

 ``` 

## Migração para o MySQL


### Ubuntu

Possívelmente vai precisar dessas bibliotecas, então digite:

```bash
sudo apt-get install libmysqlclient-dev python3-dev
```

### windows

```bash
pip install wheel mysqlclient mysql-connector-python pymysql
```

> Se der erro, verificar se esta utilizando o python x64
> o Microsoft Visual C++ 14.0 é requerido.

E depois salvar as bibliotecas usadas:

```bash
pip freeze > requirement.txt
```

Depois rodar o comando de migração:

```bash
$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
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
  Applying sessions.0001_initial... OK
```

Criar depois um novo superusuário

```bash
python manage.py createsuperuser
```

> admin:university

