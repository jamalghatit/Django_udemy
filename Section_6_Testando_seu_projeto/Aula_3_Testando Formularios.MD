# Testando Formulários

Em Projeto\core\tests\test_forms.py:

```python
from django.test import TestCase
from model_mommy import mommy
from ..forms import ContactForm

class ContactFromTestCase(TestCase):
    
    def setUp(self):
        self.name = 'john'
        self.email = 'john@john.com'
        self.subject = 'Mi chiamo John'
        self.message = 'Boungiorno'

        self.dados = {
            'name' : self.name,
            'email': self.email,
            'subject': self.subject,
            'message' : self.message,
        }

        self.form = ContactForm(data=self.dados)
        # ContatoForm(request.POST)
        # Voce vai estar recebendo via post, nesse formato de self.dados,
        # como se fosse um dicionario, json e é essa variável data é
        # a que contem nossos dados.

    def test_send_mail(self):
        form1 = ContactForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_email()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_email()

        self.assertEqual(res1, res2)
```

Rodando os testes

```bash

$ coverage run manage.py test && coverage report -m && coverage html&& cd 'htmlcov/' && python -m http.server && cd ..
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.248s

OK
Destroying test database for alias 'default'...
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
core\forms.py       15      0   100%
core\models.py      43      0   100%
core\views.py       23      9    61%   14-17, 20-22, 25-26
----------------------------------------------
TOTAL               81      9    89%
Serving HTTP on :: port 8000 (http://[::]:8000/) ...

```