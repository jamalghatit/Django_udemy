# 1. O mínimo que você precisa saber sobre CSS

CSS é a sigla de Cascading Style Sheets, ou Folha de Estilo em Cascata
e é usado para aplicar estilos nas páginas HTML.

Desenvolvido pelo W3C em 1996 para formatar páginas HTML, já que as
tags HTML form projetadas para realizar marcação das páginas.

A relação entre HTML e CSS é bem forte. Como o HTML é uma linguagem
de marcação (o alicerce de um site) e o CSS é focado no estilo (toda a
estética de um site), eles andam juntos.

Basicamente existem duas formas de se adicionar estilos CSS em uma 
página HTML.

1 - Inline, ou seja, diretamente na página HTML (**não recomendado**);

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Geek University - HTML 1</title>
        <style>
            /*
                Declaração dentro das tags.
            */
            body {
                background:navy;
                color:white;
            }
        </style>
    </head>
    <body>
        <p>Programação WEB com Django Framework</p>
    </body>
</html>
```

2 - Externo, ou seja, em arquivo externo ou mesmo diretamente da internet (recomendado):

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Geek University - HTML 1</title>
        <link rel='stylesheet' type='text/css' href='/css/estilos.css'>
    </head>
    <body>
        <p>Programação WEB com Django Framework</p>
    </body>
</html>
```

Usamos CSS para formatar nossas páginas HTML de 3 formas diferentes:

1 - **Por elemento (tag) html**: Usado quando queremos que todas as tags
especificadas recebem a mesma formatação. No arquivo css, é posto o nome da tag
e os atributos dentro de chaves {}

2 - **Por classe**: Usado quando queremos que todo elemento que incorporar
a determinada classe receba a formatação. Na página html, é posto dentro da tag
a palavra class='algumacoisa' e no arquivo css, a classe é referenciada por
.algumacoisa (ponto e o nome da classe) e os atributos dentro de chaves {}

3 - **Por id**: Usado quando queremos que elementos individuais recebem a
formatação. Na página html, é posto dentro da tag
a palavra id='algumacoisa' e no arquivo css, o id é referenciada por
\#algumacoisa (cerquilha e o nome da classe) e os atributos dentro de chaves {}

## Anatomia de um comando CSS:

Um comando básico CSS é composto por seletor e declarações que contém
propriedade e valor.

```css
SELETOR{
    propriedade: valor;
}
```

O seletor seleciona quais elementos da página receberão a formatação da propriedade
com o valor especificado. Esse seletor pode ser uma tag HTML (p, body, etc...), uma
classe (classs='blabla') ou um id (id='bla')

São muitas as propriedades e valores possíveis para formatação de uma página. Podemos
formatar praticamente qualquer coisa, lembrando que estamos falando de aplicação de 
estilos, que envolve escolher tipo/tamanho/cores de fonte, cores de página, alinhamento
posicionamento de seções e etc. Programador backend sofre com essas coisas.

Exemplo:
```css

body {
  background-color: lightblue;
}

.classe {
  color: white;
  text-align: center;
}

#id_1 {
  font-family: verdana;
  font-size: 20px;
}

```
