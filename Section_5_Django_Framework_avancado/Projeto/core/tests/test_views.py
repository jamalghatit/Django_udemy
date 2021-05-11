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
