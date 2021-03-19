# Criar uma aplicação base

$ django_admin startapp core

core/migrations -> Histórico das migrações do banco de dados</br>
core/admin.py -> Administração do site django.</br>
core/models.py -> é o arquivo onde serão criados os modelos de dados, classes que terão
seus dados persistido      s no DB ou no projeto</br>
core/tests.py -> criação de testes.</br>
core/views.py -> onde será criado as views (funções) para definir as visões.</br>
</br>

Cada aplicação criada, ir no arquivo settings.py e incluir o nome da aplicação criada na lista INSTALLED_APPS. Nesse mesmo arquivo, adicionar na lista Templates, na chave dir, o local onde terá os templates.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', # Aqui
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # Aqui
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```