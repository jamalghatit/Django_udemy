from django.shortcuts import render
from django.contrib import messages
# adiciona mensagens no contexto da pagina
# aparece essas mensagens na pagina quando declarado
# na pagina {% bootstrap_messages %}

from .forms import ContatoForms

def index(request):
    return render(request, 'index.html')

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
    return render(request, 'produto.html')

