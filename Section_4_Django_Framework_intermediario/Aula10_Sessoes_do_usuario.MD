# Trabalhando com seções do usuário

core/views.py

```python
from django.shortcuts import render, redirect

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto')
        else:
            form = ProdutoModelForm()
        context = {
            'form':form
        }
        return render(request, 'produto.html', context=context)
    else:
        return redirect('index')
```