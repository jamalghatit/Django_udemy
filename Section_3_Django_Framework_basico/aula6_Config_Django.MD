# Arquivo Settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # indica que dentro das aplicações, terá um diretório 
        '''
        Aqui é indicado onde esta a pasta em que estão localizado os templates dos 
        aplicativos.
        '''
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

Para rodar o servidor:

```python
python manage.py runserver

```

DEBUG = False

ALLOWED_HOSTS = ['*']

Quando fizer alteração no arquivo python, o django detecta automaticamente
