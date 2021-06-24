# Criando os templates

Criar a pasta templates em Section_10_Trabalhando_com_Aplicações_em_tempo_real\Projeto\chat e dentro criar os arquivos index.html.

Section_10_Trabalhando_com_Aplicações_em_tempo_real\Projeto\chat\templates\index.html:

```html
{% load bootstrap4 %}

<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Geek Chat</title>
    {% bootstrap_css %}
  </head>
  <body>
    <div class='container'>
        Qual sala de chat você gostaria de entrar?</br>
        <input id='nome_sala' name='nome_sala' type='text' size='100' placeholder='Nome da sala...'></br>
        {% buttons %}
            <input id='botao' class='btn btn-primary' type='button' value='Entrar' />
        {% endbuttons %}
    </div>
    <script>
        document.querySelector('#nome_sala').focus(); // quando a pagina carregar, o foco será nesse campo
        documento.querySelector('#nome_sala').onkeyup = function(e){ // O # indica o id.
            if(e.keyCode == 13){ //keycode == 13 é a tecla enter.
                document.querySelector('#botao').click();
            }
        };

        document.querySelector('#botao').onclick = function(e){
            var nome_sala = document.querySelector('#nome_sala').value;
            if(nome_sala != ""){
                window.location.pathname = '/chat/' + nome_sala + '/';
            }else{
                alert('Você precisa informar o nome da sala. ');
                document.querySelector('#nome_sala').focus();
            }
        }
    </script>
    {% bootstrap_javascript jquery='full' %}
  </body>
</html>

```

Section_10_Trabalhando_com_Aplicações_em_tempo_real\Projeto\chat\templates\sala.html:

```html

{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <meta charset="utf-8">
    <title>Geek Chat</title>
    {% bootstrap_css %}
  </head>
  <body>
    <div class='container'>
        <textarea id=sala cols='70' row='15'></textarea><br>
        <input id='texto' type='text' size='100'><br>
        {% bottons %}
            <input id='botao' type='button' value='Enviar' />
        {% endbuttons %}

    {% bootstrap_javascript jquery='full'%}

    <script>
        var nome_sala = {{ nome_sala_json }};

        var chatSocket = new WebSocket(
            'ws://' + window.location.host +
            '/ws/chat/' + nome_sala + '/'
        );

        chatSocket.onmessage = function(e){
            var dados = JSON.parse(e.data);
            var message = dados['message'];
            document.querySelector('#sala').value += (mensagem + '\n');
        };

        chatSocket.onclose = function(e){
            console.error("O chat encerrou de forma inesperada");
        };

        document.querySelector('#texto').focus();
        document.querySelector("#texto").onkeyup = function(e){
            if(e.keyCode == 13){
                document.querySelector('#botao').click();
            }
        };

        document.querySelector('#botao').onclick = function(e){
            var mensagemInput = document.querySelector('#texto');
            var mensagem = mensagemInput.value;
            chatSocket.sent(JSON.stringify({
                'mensagem': mensagem
            }));
            mensagemInput.value = '';
        }

    </script>
  </body>
</html>

```