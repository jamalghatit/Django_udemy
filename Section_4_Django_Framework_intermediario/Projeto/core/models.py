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