# O mínimo que voce precisa saber sobre o HTML

HTML -> Hypertext Markup Language.

Ao trabalhar com HTML, nós codificamos estruturas (tags e atributos)</br>
para marcar a página de um site, por isso o HTML é chamado de linguagem</br>
de marcação. Um arquivo HTML tem extensão  '.html'

De forma geral, uma página web é dividida em 3 áreas principais:</br>
header, body, footer

**Header**: usados para tags de informação sobre o site, aplicação de estilos css, etc.</br>
**Body**: conteúdo do site que é apresentado ao cliente.</br>
**Footer**: geralmente usado para carregamento de scripts JavaScript e apresentação de dados de rodapé.</br>
> obs.: o footer fica dentro da área de conteúdo.

Uma página web é renderizada pelo navegador de cima para baixo, linha a linha.

## Página HTML Mínima

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset = 'utf-8'>
    <title> Geek Univesity - HTML 1 </title>
</head>
<body>
    <p> Programação Web com Django Framework</p>
</body>
</html>

```

> Obs: podemos iniciar um servidor web simples com Python
> utilizando o comando:

```bash
python3 -m http.server 8000
# utiliza esse -m para importar um módulo
```

Obs:

- As tags HTML formam uma hierarquia de elementos.
- Algumas tagas abrem, mas não fecham.

As tags HTML são subdivididas em dois grupos principais:</br>
**Elemento de bloco**: Utilizam todo o espaço disponível e começam</br>
uma nova linha no documento.
Exemplo:

```html
<html></html> 
<head></head>
<h1></h1>
...
<h6></h6>
<div></div> - Divisões de seção de conteúdo
<p></p> - paragrafo
<blockquote></blockquote> - Bloco de citações
<ol></ol> - Listas ordenadas
<ul></ul> - Listas não ordenadas
<li></li> - Lista de itens

```

**Elemento em linha**: Utilizam apenas o espaço necessário e não
criam uma quebra de linha.

```html
<strong></strong> - Renderiza o texto em negrito.
<em></em> - Renderiza o texto em itálico
<a></a>: Cria um link para outra página ou documento.
<img> Adiciona image na página.
```
