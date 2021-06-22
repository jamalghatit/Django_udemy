# Aproveitando os recursos do Django Models

**Entidade forte** - entidade independente, não tem chave estrangeira. Ela por si só existe.
Ex: Classe Chassi, Montadora

```python
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

```

**Entidade fraca** - Criação dependente. Há chave estrangeira.
Ex: Carro depende de chassi e montadora.

```python

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
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo', max_length=32, help_text='Max 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.montadora} {self.modelo}'

```

Nos relacionamentos um para um e um para muitos (OneToOneField e ForeignKey), é
necessário colocar on_delete.

```python
montadora = models.ForeignKey('Montadora', on_delete=models.CASCADE)

montadora = models.ForeignKey('Montadora', on_delete=models.SET_DEFAULT, default=1)

```

Em models (Section_9_Relacionamento_entre_modelos\django_orm\core\models.py):

```python

def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0]
    # Retorna (objeto, boolean)

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
    montadora = models.ForeignKey('Montadora', on_delete=models.SET(set_default_montadora)) #
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo', max_length=32, help_text='Max 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

```
Shell:

```python

>>> from core.models import Montadora
>>> resultado = Montadora.objects.get_or_create(nome='Fiat')
>>> resultado
(<Montadora: Fiat>, True)

# Como já fora criado, ele retorna false.
>>> resultado = Montadora.objects.get_or_create(nome='Fiat')
>>> resultado
(<Montadora: Fiat>, False)

>>> resultado = Montadora.objects.get_or_create(nome='Fiat')[0]
>>> resultado
<Montadora: Fiat>

```

Mostrar ManyToManyField:

Em Section_9_Relacionamento_entre_modelos\django_orm\core\admin.py:

```python

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('montadora', 'modelo', 'chassi', 'preco', 'get_motoristas')

    def get_motoristas(self, obj):
        return ', '.join([m.username for m in obj.motoristas.all()])

    get_motoristas.short_description = 'Motoristas'

```

Shell:

```python
>>> from core.models import Carro

>>> carro1 = Carro.objects.get(pk=2) 
>>> resultado = [ m.username for m in carro1.motoristas.all()]
>>> resultado
['geek', 'tião']
>>> ', '.join(resultado)
'geek, tião'

```