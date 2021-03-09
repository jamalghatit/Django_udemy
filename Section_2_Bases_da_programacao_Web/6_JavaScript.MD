# O mínimo que você precisa saber sobre javaScript

A linguagem JavaScript foi criada por Brendan Eich na empresa Netscape.

Atualmente é mantida pela European Computer Manufacturer's Association
e seu nome "oficial" é ECMAScript, mas continua sendo mais conhecida, 
principalmente pelos mais leigos, como JavaScript.

>Obs: O javaScript não é java.

O JavaScript completa a tríade da web se encarregando dos comportamentos
e ações das páginas.

HTML -> Estrutura</br>
CSS -> Estilo;</br>
JavaScript -> Comportamentos/ações;</br>

Obs: é aconselhavel colocar `<script type="text/javascript" src="js/scripts.js"></script>`
no final do arquivo, pois evita de se ter erros, pois a página já foi toda renderizada.

Exemplo HTML:

```html

<!DOCTYPE html>
<html>
    <head>
        <title>Geek University - Javascript 1</title>
        <meta http-equiv="Content-Type" content="text/html;" charset="utf-8">
    </head>
    <body>
        <div>
            <center>
                <h1>Geek University</h1>
                <button onclick="gritar();">clique em mim</button>
                <br/>
                <br/>
                <button onclick="perguntar();"> questionario</button>
                <br/>
                <br/>
                <button onclick="mudar_texto();">Muda h1</button>
                <br/>
                <br/>
                <button onclick="incrementar();">incrementar</button>
                <p id="p1">0</p> 
            </center>
        </div>
        <script type="text/javascript" src="js/scripts.js"></script>
    </body>
</html>

```


Exemplo JavaScript:

```javascript

function gritar(){
    alert('aaaaaaaaaaaaaaaaaaahhhh');
}

function perguntar(){
    var nome;
    nome = prompt('Qual é o seu nome?')
    alert('Olá ' + nome)
}

function mudar_texto() {
    var h1 = document.getElementsByTagName('h1');
    if(h1[0].innerText == 'Geek University'){
        h1[0].innerText = "Evolua seu lado geek!";
    }else{
        h1[0].innerText = 'Geek University';
    }
}

function incrementar() {
    var p1 = document.getElementById('p1');
    p1.innerText = parseInt(p1.innerText) + 1;
}



```
