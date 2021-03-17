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
pip install mysqlclient mysql-connector-python pymysql
```

> o Microsoft Visual C++ 14.0 é requerido.

E depois salvar as bibliotecas usadas:

```bash
pip freeze > requirement.txt
```

Depois rodar o comando de migração:

```bash
python manage.py migrate
```