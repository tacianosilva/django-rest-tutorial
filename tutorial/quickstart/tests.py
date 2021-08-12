from django.test import TestCase
from django.contrib.auth.models import User, Group
import requests
from rest_framework.authtoken.models import Token

class TokenAuthenticationTests(TestCase):
    """Classe de testes do uso de TokenAuthentication."""

    def setUp(self):
        self.username = 'admin'
        self.password = '12345'
        self.admin = User.objects.create(
            username=self.username, password=self.password)

    def test_token_create(self):
        token = Token.objects.create(user=self.admin)
        self.assertIsNotNone(token)

    def test_authentication(self):
        url = 'http://localhost:8000/api-token-auth/'
        # You have to POST username and password to /api-token-auth/ - to obtain an authentication token.
        data = {'username': self.username, 'password': self.password}
        response = requests.post(url, data)
        print(response.status_code)
        print(response.json().get('token'))
        token = response.json().get('token')

        headers = { 'Content-Type': 'application/json', 
                    'Accept': 'application/json', 
                    'Authorization': 'Token ' + token}

        url = "http://localhost:8000/users/"
        response = requests.get(url, headers=headers)
        print(response.status_code)
        print(response.json().get('results'))
        print(response.json().get('results')[0].get('username'))
        print(response.json().get('results')[0].get('groups'))
