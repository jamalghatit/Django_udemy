# Entendendo e configurando os testes

Em Projeto\core\tests.py:

```python

def add_num(num):
    return num + 1

class SimplesTestCase(TestCase):

    # roda toda vez
    def setUp(self):
        self.numero = 41
        print('iniciando o testcase')

    # Testa a unidade de codigo todo o teste começa com 'test_'
    # O gerenciador de testes vai procurar classes que hendem de TestCase e vai
    # testar as funções iniciadas ou terminadas com test_ ou _test.

    def test_add_num(self):
        valor = add_num(41)
        self.assertTrue(valor == 42)

    # Toda vez que é rodado o teste, é criado um novo banco de dados de teste e ao
    #final  ele deleta o DB de teste.
```

Para rodar os testes:

```bash

$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
iniciando o testcase
.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
Destroying test database for alias 'default'...
(venv)

```

Apagar o arquivo test.py e criar um diretório tests em
Projeto\core, e criar um arquivo chamado \_\_init\_\_,
indicando para o python que esse diretório é um pacote python.
E dentro dessa pasta, criar um arquivo de teste para cada classe.

Dentro da pasta, criar os arquivos:
test_forms.py, test_models.py, test_views.py

## Ferramentas de auxilio de teste

Instalar o model_mommy  e coverage:

```python

pip install model_mommy coverage

pip freeze > requirements.txt
```

Criar um arquivo chamado .coveragerc:

```text
[run]
source = .

omit =
     */__init__.py
     */settings.py
     */manage.py
     */wsgi.py
     */asgi.py
     */apps.py
     */urls.py
     */admin.py
     */migrations/*
     */tests/*

```

Para rodar o teste com coverage: ` coverage run manage.py test`

```bash
$ coverage run manage.py test
System check identified no issues (0 silenced).

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
(venv)
```

Para ver o relatório do coverage: `coverage report`

```bash

$ coverage report
Name             Stmts   Miss  Cover
------------------------------------
core\\forms.py       15      7    53%
core\\models.py      41      5    88%
core\\views.py       23      9    61%
------------------------------------
TOTAL               79     21    73%
(venv)

```

Ir em Projeto\.gitignore para ignorar o arquivos da pasta htmlcov:

```text
htmlcov/*

```

Para gerar um html com percentual de cobertura:
`coverage html`

Depois entre na pasta htmlcov e rode o servidor nela:
`python -m http.server`

