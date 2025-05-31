import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
    # Criação do cliente de teste
        cls.client = app.test_client()

    def test_get_items(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.json['items']), type([]))
    
    def test_protected_route(self):
        response_login = self.client.post('/login')
        token = response_login.json['access_token']

        response = self.client.get('/protected', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Protected route"})

    def test_wrong_token_protected(self):
        incorrect_token = 'esse.token.esta.incorreto'
        response = self.client.get('/protected', headers={'Authorization': f'Bearer {incorrect_token}'})

        self.assertEqual(response.status_code, 422)

if __name__ == '__main__':
    unittest.main()