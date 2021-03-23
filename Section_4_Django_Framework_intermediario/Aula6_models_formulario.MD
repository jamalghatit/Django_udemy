# Definindo e configurando os models

---

**Slug** é a parte de uma URL que pode ser legível tanto para humanos quanto para mecanismos de busca. É, normalmente, parte da URL de páginas em sistemas que fazem uso de URL amigável.
O slug do texto "A rápida raposa marrom pula sobre o cão preguiçoso" ficaria "a-rapida-raposa-marrom-pula-sobre-o-cao-preguicoso". Alguns sistemas, como o WordPress, permitem a edição dos slugs para que fique à escolha do usuário

---

core/models.py:

```python

from django.db import models
from stdimage.models import StdImageField

#SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateTimeField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    # Classe abstrata não é criada no banco de dados.
    # Ela servirá como rascunho para outras classes.
    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField("Nome", max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124,124)})
    slug = models.SlugField("Slug", max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome


def produto_pre_save(signal, instance, sender, **kwargs):
    '''
    Aplica o slug no nome do produto e salva na 
    variável slug dentro da instancia.
    ex: 
    nome: maria mole do sertão
    slug: maria-mole-do-sertao
    '''
    instance.slug = slugify(instance.nome)

# Antes de salver, executa a função produto_pre_save,
# quando a objeto Produto enviar o sinal, ou seja,
# Quando a objeto produto for salvo, essa função 
# signals.pre_save.connect, será chamada.
signals.pre_save.connect(produto_pre_save, sender=Produto)

```

Depois realizar as fazer e realizar as migrações:

```bash
$ python manage.py makemigrations
Migrations for 'core':
  core\migrations\0001_initial.py
    - Create model Produto

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, core, sessions
Running migrations:
  Applying core.0001_initial... OK

```

core/admin.py

```python

from django.contrib import admin

from .models import Produto
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'slug', 'criado', 'modificado', 'ativo')

"""
@admin.register(Produto) ou
admin.site.register(Produto, ProdutoAdmin)
"""

```

---

## Abstract base classes

Abstract base classes are useful when you want to put some common information into a number of other models. You write your base class and put **abstract=True** in the Meta class. This model will then not be used to create any database table. Instead, when it is used as a base class for other models, its fields will be added to those of the child class.

An example:

```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```

The Student model will have three fields: name, age and home_group. The CommonInfo model cannot be used as a normal Django model, since it is an abstract base class. It does not generate a database table or have a manager, and cannot be instantiated or saved directly.

Fields inherited from abstract base classes can be overridden with another field or value, or be removed with None.

For many uses, this type of model inheritance will be exactly what you want. It provides a way to factor out common information at the Python level, while still only creating one database table per child model at the database level.

---