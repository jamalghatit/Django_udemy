# Testando Models

No shell (python manage.py shell):

```bash
>>> from model_mommy import mommy
>>> cargo = mommy.make('Role')
>>> cargo.role
'IMwtiFzWXiQQyHTKCLgthoqLYiWHhGDjzmyXsxgQyvkTfxnWzCYuJrledzlDLkpUYDZGvxXMbjClztKgMMFcWfMEWgxNBbFihkmr'
>>> cargo.role = 'designer'
>>> cargo.role
'designer'
>>> cargo.save()

>>> services = mommy.make('Service', _quantity=5)
>>> services[
<Service: qaNpKrPLiSLQnbTShtoNAaOfIlDdwynXdxlOFzfjdStaChXVvySfiTKUlbXlMEgKKfpnjizUXQrGaArkBKHBGNCUEUAYdeLrPhmg>,
<Service: HugyHvGHhYiuROGGFzAyBEqadFBBTDLGZDwTAnbMXRFFQNQglOZZthUtaQAgWeghjzsXAnSaIIDvoimKLKccoRsmhwTKgMWhjgOf>,
<Service: wuTzSIsgqxPPPNNhqgFKFDdMAxaThVXQrXsWOWEhdJfAtXNYputFjNSzosPpOerrgMhIMRakvAUOYpXqloxHtEwaPNnqKsfUebZd>,
<Service: tqUzCsJmOcRnqDBBYTYoLzwCxfkZSqGBUgmHdNxPTbYMErjiBrHuDwEkYHsDsabhuqhYLMssNlGGrngOpLvZvUsdYbvklBDJWdej>,
<Service: LQFpwphGVGsuIRCAXYpTzHAfkXkzXMEVoEaMSzlmPAhrlqyfPzyXtfPSczzKulbHMlsevrBsrBfypwqQwhGTqtuRnpUaLmrwDzQv>
]

>>> services[0].services
'qaNpKrPLiSLQnbTShtoNAaOfIlDdwynXdxlOFzfjdStaChXVvySfiTKUlbXlMEgKKfpnjizUXQrGaArkBKHBGNCUEUAYdeLrPhmg'
>>> services[0].icon
'lni-stats-up'
>>> services[0].description
'fTmApKSUfwibOSZPSCkEwSUuHbrwMIJCPtqFGvxJAqBcCXVdbYCPSfeAHEvHAHcPBferJEDbzLOnMTwBgBPSiNgrtgrMrQriMxuuhOsqTLbabWfrjVdlCErcXKVouUsNPlXOOeAOpIPfxtclkCCEGJjJXTOZThYqYQWQeCyEsnOoKPZfvrMMpcFUpHHVwwLYHFFmTyiyrrBHyuuOphgxanTkMvpxJPdrTotZcRKWnRuXImALfIVAbXwoyaPoMTUdEJSCMhbGpRiQNkjhOrwmbmSxQKMbFcGVjAaRfxMYPeXw'

# O mommy colocou a string com o tamanho maximo permitido, por exemplo, description = models.TextField('Description', max_length=200)

>>> team = mommy.make('Team', _quantity=3)
>>> team[0]
<Team: Team object (5)>
>>> team[0].role
<Role: dMfSWxIOXqqhBqNjHqOKDCeDXgLrbWXeqKRPYEXzCVYmUHYfyeYCJjaHYRRwkJloWmLtRsiydGSbQeHzXnkcyiPwKdQVjmxuqiPV>

```

Em Projeto\core\tests\test_models.py:

```python
import uuid
from django.test import TestCase
from model_mommy import mommy

from ..models import get_file_path

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


```

No bash:

```bash
>>> import uuid
>>> filename = f'\{uuid.uuid4()}.png'
>>> filename
'5f08f0ff-3823-454b-877e-e809cfe7135a.png'
>>> len(filename)
40
>>> arquivo = get_file_path(None, 'teste.png')
>>> arquivo
'a4646ebc-3990-4c96-8335-08144d2a1bf0.png'
>>> len(arquivo)
40

```

Para rodar os testes:

```bash

$ coverage run manage.py test && coverage report -m && coverage html\
&& cd 'htmlcov/' && python -m http.server && cd ..

Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
Destroying test database for alias 'default'...
Name             Stmts   Miss  Cover   Missing
----------------------------------------------
core\\forms.py       15      7    53%   12-26
core\\models.py      41      2    95%   38, 48
core\\views.py       23      9    61%   14-17, 20-22, 25-26
----------------------------------------------
TOTAL               79     18    77%
(venv)


```

**Para cada model, cria-se um testcase.**

```python
import uuid
from django.test import TestCase
from model_mommy import mommy

from ..models import get_file_path

class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))

class ServiceTestCase(TestCase):

    def setUp(self):
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertEqual(str(self.service), self.service.services)

class RoleTestCase(TestCase):

    def setUp(self):
        self.role = mommy.make('Role')

    def test_str(self):
        self.assertEqual(str(self.role), self.role.role)

```