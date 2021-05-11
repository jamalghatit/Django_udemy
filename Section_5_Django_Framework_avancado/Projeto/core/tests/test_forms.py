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
