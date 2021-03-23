# 42. Trabalhando com formulários parte 2 - ModelForms

Dois tipos de forms -> os que tem e que não tem conexão
com o banco de dados.

Para cada formulário, terá uma classe no forms.py:

```python

from .models import Produto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        '''
        Passando os metadados.
        '''
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']

```

core/views.py:

```python

def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=false)

            print(f'Nome: {prod.nome}')
            print(f'Preço: {prod.preco}')
            print(f'Estoque: {prod.estoque}')
            print(f'Imagem: {prod.imagem}')

            messages.success(request, 'Produto salvo com sucesso')
        else:
            messages.error(request, 'Erro ao salvar produto')
    else:
        form = ProdutoModelForm()

    context = {
        'form':form
    }
    return render(request, 'produto.html', context=context)

```

produto.html:

```html

{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <title>Produto</title>
    <meta charset="utf-8">
    {% bootstrap_css %}
  </head>
  <body>
    <div class = 'container'>
      <h1>Produto</h1>
      {% bootstrap_messages %}

      <form action='{% url "produto" %}' method='post' class='form' autocomplete="off" enctype="multipart/form-data">
        {% csrf_token %}

        {% bootstrap_form form %}
        {% buttons %}
          <button type='submit' class='btn btn-primary'>Cadastrar</button>
        {% endbuttons %}
      </form>
    </div>

    {% bootstrap_javascript jquery='full' %}
</body>
</html>

```