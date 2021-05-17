# Criando um User Model Customizado

Criar um novo projeto em Section_7_Djanto_User_Model/Projeto:

```bash

\$ django-admin startproject django_user_model_customizado
\$ django-admin startapp usuarios
```

Em Projeto\django_user_model_customizado\django_user_model_customizado\settings.py:

```python


INSTALLED_APPS = [
    'usuarios', #
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], #
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

LANGUAGE_CODE = 'pt-br' #

TIME_ZONE = 'America/Sao_Paulo' #


MEDIA_ROOT = '/media/' #
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #

AUTH_USER_MODEL = 'usuarios.CustomUsuario' #

```

Em Section_7_Djanto_User_Model\Projeto\django_user_model_customizado\usuarios\models.py:

```python
from django.db import models

# from django.contrib.auth.models import AbstractBaseUser
# AbstractBaseUser é um módulo mais basico, ou seja,
# diversas implementações teram que ser feitas na mão.
# Já o AbstractUser é mais completa
from django.contrib.auth.models import AbstractUser, BaseUserManager

# BaseUserManager - é o gerenciador de usuario que gerenciará o usuario customizado.

class UsuarioManager(BaseUserManager):

    use_in_migrations = True
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        
        return self._create_user(email, password, **extra_fields)

class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']
    
    def __str__(self):
        return self.email
    
    objects = UsuarioManager() 
    # aqui especifica qual é a classe que gerencia esse objeto (CustomUsuario).
    # Pois se não for especificado, ele será gerenciado pelo default do django

    def __str__(self):
        return self.email

```

Em Section_7_Djanto_User_Model\Projeto\django_user_model_customizado\usuarios, 
criar o arquivo forms.py:

```python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUsuario

class CustomUsuarioCreateForm(UserCreationForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        # cleaned_data é utilizado para acessar o dado do form.
        if commit:
            user.save()
        return user

class CustomUsuarioChangeForm(UserChangeForm):

    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')

```

Em Section_7_Djanto_User_Model\Projeto\django_user_model_customizado\usuarios\admin.py:

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario

@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')})
        ('Datas importantes', {'fields' : ('last_login' , 'date_joined') })
    )

```

Se tiver tudo certo:

```bash

\$ python manage.py makemigrations
\$ python manage.py migrate

\$ python manage.py createsuperuser

E-mail: geek@geek.com.br
Primeiro nome: geek
Último nome: geek
Telefone: 129662665
Password:
Password (again):
Superuser created successfully.

```