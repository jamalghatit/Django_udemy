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

class TeamTestCase(TestCase):

    def setUp(self):
        self.team = mommy.make('Team')

    def test_str(self):
        self.assertEqual(str(self.team), self.team.name)