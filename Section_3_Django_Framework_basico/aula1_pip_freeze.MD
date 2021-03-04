# Comandos do PIP

## pip freeze

Output installed packages in requirements format.
packages are listed in a case-insensitive sorted order.

Esse comando salva todos os nomes das bibliotecas que estão sendo utilizadas no projeto.

`pip freeze > requirements.txt`

Para instalar em outro ambiente:

`python -m pip install -r requirements.txt`

