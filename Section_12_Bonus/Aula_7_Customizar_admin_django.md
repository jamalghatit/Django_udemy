# Customizando, ainda mais, o admin do Django

Essa aula irá utilizar o ambiente da Aula_6_paginação.

EmAula_6_paginação\paginacao\paginacao\urls.py:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),   
]

admin.AdminSite.site_header = 'Sistema XPTO'
admin.AdminSite.site_title = 'Geek University'
admin.AdminSite.index_title = 'Meu sistema super legal'
```

- Instalar:

```bash
pip install django-adminlte2

```

Em Aula_6_paginação\paginacao\paginacao\settings.py:

```python
INSTALLED_APPS = [
    'django_adminlte', # É colocado acima para poder sobreescrever os demais.
    'django_adminlte_theme', # É colocado acima para poder sobreescrever os demais.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'bootstrap4',
]
```

Acessar Aula_6_paginação\venv\Lib\site-packages\django\contrib\admin\templates\admin e copiar essa pasta e colar em Aula_6_paginação\paginacao\templates\admin.

Ao colocar a pasta com nome admin dentro da pasta template do projeto, voce altera o template do admin.

---

Copiar as pastas:

- Aula_6_paginação\venv\Lib\site-packages\django_adminlte_theme\templates\admin para Aula_6_paginação\paginacao\templates\admin e 
- Aula_6_paginação\venv\Lib\site-packages\django_adminlte\templates\adminlte para Aula_6_paginação\paginacao\templates\adminlte

e customizar da forma que desejar.
