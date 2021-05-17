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

