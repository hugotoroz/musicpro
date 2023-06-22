import pytest
from django.test import Client, TestCase
from store.models import Category
from django.urls import reverse


class test_carga_index(TestCase):
    def setUp(self):
        self.client = Client()

    def test_template_content(self):
        response = self.client.get('')
        assert response.status_code == 200

class test_carga_carrito(TestCase):
    def setUp(self):
        self.client = Client()

    def test_template_content(self):
        response = self.client.get('/basket/')
        assert response.status_code == 200

class test_carga_login(TestCase):
    def setUp(self):
        self.client = Client()

    def test_template_content(self):
        response = self.client.get('/cuenta/login/')
        assert response.status_code == 200
class test_carga_registro(TestCase):
    def setUp(self):
        self.client = Client()

    def test_template_content(self):
        response = self.client.get('/cuenta/signup/')
        assert response.status_code == 200

class test_buscar_categoria_fallido(TestCase):
    def setUp(self):
        self.client = Client()

    def test_template_content(self):
        response = self.client.get('/search/guitarras')
        assert response.status_code == 301
class test_buscar_url_fallido(TestCase):
    def setUp(self):
        self.client = Client()

    def test_template_content(self):
        response = self.client.get('/urlquenoexiste/')
        assert response.status_code == 404