# Introdução

Dentro do venv do projeto fusion (Section_5_Django_Framework_avancado\Projeto):
`pip install textblob`

No bash:

```python
>>> from textblob import TextBlob
>>> texto = TextBlob('Evolua seu lado geek!')
>>> texto.translate(to='en')
TextBlob("Evolve your geek side!")
>>> texto.translate(to='es') 
TextBlob("¡Desarrolla tu lado friki!")


```