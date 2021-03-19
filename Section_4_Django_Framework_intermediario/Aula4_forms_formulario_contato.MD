# Trabalhando com formulários parte 1 - Forms

Todos os formulários são criados dentro do arquivo forms.py

Criar arquivo forms.py (core/forms.py)

```python

from django import forms

class ContatoForms(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

```

view.py(core/view.py):

```python

from .forms import ContatoForms

def contato(request):

    form = ContatoForms()
    """
    Tudo aquilo que quiser enviar no contexto do template,
    é colocado nesse dicionário
    """
    context = {
        'form' : form
    }
    return render(request, 'contato.html', context=context)
    
    ```

Adcionar modificação no template/contato.html:

```html

{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <title>Contato</title>
    <meta charset="utf-8">
    {% bootstrap_css %}
  </head>
  <body>
    <div class='container'>
    <h1>Contato</h1>
    {% bootstrap_messages %}

      <form action="{% url 'contato' %}" method='POST' class='form' autocomplete='off'>
        {% csrf_token %}
        {% bootstrap_form form%} # <!-- esse é o contexto form passado na view.py-->
        {% buttons %}
        <!-- -->
          <button type='submit' class='btn btn-primary'>Enviar Mensagem</button>
        {% endbuttons %}
      </form>
    </div>
{% bootstrap_javascript jquery='full'%}
</body>
</html>

```

## Django-bootstrap

-----
After Installation, you can use django-bootstrap3 in your templates.:

Load the bootstrap3 library and use the bootstrap_* tags:

```html

Example template
{# Load the tag library #}
{% load bootstrap3 %}

{# Load CSS and JavaScript #}
{% bootstrap_css %}
{% bootstrap_javascript %}

{# Display django.contrib.messages as Bootstrap alerts #}
{% bootstrap_messages %}

{# Display a form #}
<form action="/url/to/submit/" method="post" class="form">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% buttons %}
    <button type="submit" class="btn btn-primary">
      {% bootstrap_icon "star" %} Submit
    </button>
  {% endbuttons %}
</form>

{# Read the documentation for more information #}
```

----

core/view.py:

```python

def contato(request):
    form = ContatoForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviado')
            print(f'Nome: {nome}')
            print(f'email: {email}')
            print(f'assunto: {assunto}')
            print(f'mensagem: {mensagem}')
            print(f'{form})

            messages.success(request, 'Email enviado com sucesso!')
            form = ContatoForms() # aqui ele vai "resetar" a variavel 

        else:
            messages.error(request, 'Erro ao enviar e-mail')
    """
    Tudo aquilo que quiser enviar no contexto do template,
    é colocado nesse dicionário 
    """
    context = {
        'form' : form
    }
    return render(request, 'contato.html', context=context)

```

O método clened_data está pegando do variavel '**name**' do HTML.
Esse cleaned_data é uma propriedade na qual se pega por meio da chave, o valor do campo

```html
<div class="form-group"><label for="id_nome">Nome</label><input type="text" **name**="nome"
 maxlength="100" class="form-control" placeholder="Nome" title="" required id="id_nome"></div>
```

Console shell do django(python manage.py shell):

```python

>>> from django import forms
>>> dir(forms.Form)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__html__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_clean_fields', '_clean_form', '_html_output', '_post_clean', 'add_error', 'add_initial_prefix', 'add_prefix', 'as_p', 'as_table', 'as_ul', 'base_fields', 'changed_data', 'clean', 'declared_fields', 'default_renderer', 'errors', 'field_order', 'full_clean', 'get_initial_for_field', 'has_changed', 'has_error', 'hidden_fields', 'is_multipart', 'is_valid', 'media', 
'non_field_errors', 'order_fields', 'prefix', 'use_required_attribute', 'visible_fields']
>>> help(forms.Form.is_valid)
Help on function is_valid in module django.forms.forms:

is_valid(self)
    Return True if the form has no errors, or False otherwise.
```

