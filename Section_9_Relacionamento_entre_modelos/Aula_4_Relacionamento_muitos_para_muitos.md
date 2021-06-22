# Relacionamento Muitos para Muitos

Em Section_9_Relacionamento_entre_modelos\django_orm\core\models.py:

```python

from django.db import models
from django.contrib.auth import get_user_model # Acrescentar esse

class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Max 16 caracteres')

    class Meta:
        verbose_name: 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero

class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name: 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome

class Carro(models.Model):
    """
    # OneToOneField
    Cada carro só pode se relacionar com um Chassi e
    cada Chassi só pode se relacionar com um carro.

    # ForeignKey (One to Many)
    Cada carro tem uma montadora, mas uma montadoras
    pode 'montar' vários carros.

    # ManyToMany
    Um carro pode ser dirigido por vários motoristas
    e um motorista pode dirigir diversos carros.
    """
    chassi = models.OneToOneField('Chassi', on_delete=models.CASCADE)
    montadora = models.ForeignKey('Montadora', on_delete=models.CASCADE)
    motoristas = models.ManyToManyField(get_user_model()) # Acrescentar esse
    modelo = models.CharField('Modelo', max_length=32, help_text='Max 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'


```

Shell:

```bash

>>> from core.models import Carro
>>> carros = Carro.objects.all()
>>> carros
<QuerySet [<Carro: Honda City>, <Carro: Honda Fit>]>

>>> carro1 = carros.last()

>>> motorista1 = carro1.motoristas.all()
>>> motorista1
<QuerySet [<User: geek>, <User: tião>]>

>>> m1 = motorista1.first()
>>> m1
<User: geek>

>>> carros = Carro.objects.filter(motoristas=m1)
>>> carros
<QuerySet [<Carro: Honda Fit>, <Carro: Honda City>]>

#
>>> carros = Carro.objects.filter(motoristas__in = motorista1)
>>> carros
<QuerySet [<Carro: Honda Fit>, <Carro: Honda City>, <Carro: Honda Fit>]>

# Distinct retorna valores únicos quando a query traz resultados duplicados.
>>> carros = Carro.objects.filter(motoristas__in = motorista1).distinct()
>>> carros
<QuerySet [<Carro: Honda Fit>, <Carro: Honda City>]>


```