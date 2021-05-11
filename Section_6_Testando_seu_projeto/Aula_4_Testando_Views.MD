# Testando Views

Para cada view, criamos uma classe TestCase

```python
from django.test import TestCase
from django.test import Client

from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    
    def setUp(self):
        self.dados = {
            'name' :'john',
            'email': 'john@john.com',
            'subject':'Mi chiamo John',
            'message' : 'Boungiorno',
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)
        # Se o request tiver status code 302, significa que
        # Foi efetuado com sucesso e foi redirecionado para o index,
        # conforme implementação na view.
    
    def test_form_invalid(self):
        dados = {
            'name' :'john',
            'email': 'john@john.com',
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)


```
Reverse and Reverse_lazy are two utility functions that we use in our Django projects or apps to redirect from a view to another, basically it’s a more convenient way to deal with urls without hardcoding them.


Rodando os testes:

```bash

$ coverage run manage.py test && coverage report -m && coverage html&& cd 'htmlcov/' && python -m http.server && cd ..
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.......
----------------------------------------------------------------------
Ran 7 tests in 0.213s

OK
Destroying test database for alias 'default'...
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
core\\forms.py       15      0   100%
core\\models.py      43      0   100%
core\\views.py       23      0   100%
----------------------------------------------
TOTAL               81      0   100%
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```