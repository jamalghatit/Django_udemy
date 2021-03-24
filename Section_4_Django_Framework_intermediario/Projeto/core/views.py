from django.shortcuts import render, redirect
from django.contrib import messages
# adiciona mensagens no contexto da pagina
# aparece essas mensagens na pagina quando declarado
# na pagina {% bootstrap_messages %}

from .forms import ContatoForms, ProdutoModelForm
from  .models import Produto

def index(request):
    context ={
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context=context)

def contato(request):
    form = ContatoForms(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Email enviado com sucesso!')
            form = ContatoForms()
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
