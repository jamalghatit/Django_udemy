# Relacionamento Um para Muitos

Em Section_9_Relacionamento_entre_modelos\django_orm\core\models.py adicionar esse código:


```python

class Montadora(models.Model): #
    nome = models.CharField('Nome', max_length=50)#

    class Meta: #
        verbose_name: 'Montadora' #
        verbose_name_plural = 'Montadoras' #

    def __str__(self): #
        return self.nome #

class Carro(models.Model):
    """
    # OneToOneField
    Cada carro só pode se relacionar com um Chassi e
    cada Chassi só pode se relacionar com um carro.

    # ForeignKey (One to Many)
    Cada carro tem uma montadora, mas uma montadoras
    pode 'montar' vários carros.
    """
    chassi = models.OneToOneField('Chassi', on_delete=models.CASCADE)
    montadora = models.ForeignKey('Montadora', on_delete=models.CASCADE)
    modelo = models.CharField('Modelo', max_length=32, help_text='Max 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'

```

Section_9_Relacionamento_entre_modelos\django_orm\core\admin.py:

```python

@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco')
```

Django-shell:

```python

>>> from core.models import Carro
>>> carro = Carro.objects.all()
>>> carro
<QuerySet [<Carro: Honda City>, <Carro: Honda Fit>]>
>>> print(carro.query)
SELECT "core_carro"."id", "core_carro"."chassi_id", "core_carro"."montadora_id", "core_carro"."modelo", "core_carro"."preco" FROM "core_carro"

>>> fit = Carro.objects.get(pk=2)
>>> fit
<Carro: Honda Fit>
>>> fit = Carro.objects.get(modelo='Fit')
>>> fit
<Carro: Honda Fit>

>>> fit = Carro.objects.filter(modelo='Fit')
>>> fit
<QuerySet [<Carro: Honda Fit>]>

>>> print(fit.query)
SELECT "core_carro"."id", "core_carro"."chassi_id", "core_carro"."montadora_id", "core_carro"."modelo", "core_carro"."preco" FROM "core_carro" WHERE "core_carro"."modelo" = Fit

# Quando for objeto queryset, pode aplicar o first() ou o last()
>>> fit = Carro.objects.filter(modelo='Fit').first()


>>> from core.models import Montadora
>>> honda = Montadora.objects.get(pk=1)
>>> honda
<Montadora: Honda>
>>> carros = honda.carro_set.all()
>>> carros
<QuerySet [<Carro: Honda City>, <Carro: Honda Fit>]>
>>> print(carros.query)
SELECT "core_carro"."id", "core_carro"."chassi_id", "core_carro"."montadora_id", "core_carro"."modelo", "core_carro"."preco" FROM "core_carro" WHERE "core_carro"."montadora_id" = 1

>>> carros.first()
<Carro: Honda City>
```