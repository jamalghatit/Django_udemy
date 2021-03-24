# Apresentando dados do banco de dados no template

core/view.py:

```python

from  .models import Produto

def index(request):
    context ={
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context=context)
```

core/templates/index.html:

```html
{% load bootstrap4 %}
{% load static %}
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <title>Index</title>
    <meta charset="utf-8">
    {% bootstrap_css %}
    <link rel="stylesheet" href='{% static "css/styles.css" %}'>
  </head>
  <body>
    <div class='container'>
      <h1>Produtos</h1>

      <table class='table table-dark'>
        <!-- https://getbootstrap.com/docs/4.1/content/tables/ -->
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Produto</th>
            <th scope="col">Preço</th>
            <th scope="col">Estoque</th>
          </tr>
        </thead>
        <tbody>
          {% for produto in produtos %}
            <tr>
              <td scope="row">{{ produto.id }}</td>
              <td scope="row"><a href="#modal{{produto.id}}" data-toggle='modal'>{{ produto.nome }}</a></td>
              <td scope="row">{{ produto.preco }}</td>
              <td scope="row">{{ produto.estoque }}</td>
            </tr>
            <!--https://getbootstrap.com/docs/4.1/components/modal/#vertically-centered-->
            <div class='modal fade bd-example-modal-lg show' id='modal{{produto.id}}' role='dialog'>
              <div class='modal-dialog'>
                  <div class='modal-content'>
                    <div class="modal-header">
                      <button type='button' class='close' data-dismiss='modal'>
                        <span aria-hidden='true'>&times;</span>
                      </button>
                    </div>
                    <div class='modal-body' id='dynamic.content'>
                      <img src='{{ produto.imagem.url }}' class='img-fluid' alt='{{ produto.nome }}'/>
                  </div>
                </div>
              </div>
            </div>
          {% endfor %}
        </tbody>
      </table>
    </div>
  {% bootstrap_javascript jquery='full' %}
</body>
</html>
```

core/static/css:

```css

a{
    color:white;
}

```