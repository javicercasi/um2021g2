import unittest
from django.test import Client
from .forms import SignUpFormUser, SignInForm


# Create your tests here.
class SimpleTest(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_GET_status_OK(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_signin_GET_status_OK(self):
        response = self.client.get('/signin/')
        self.assertEqual(response.status_code, 200)

    def test_signup_GET_status_OK(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_SignUpUserForm_true(self):
        data = {
            'username': 'TestDeUsuario',
            'firstName': 'Usuario',
            'lastName': 'Para Testear',
            'email': 'esteesunmail@mail.com',
            'phone': '02613893777',
            'birthday': '2000-05-09',
            'bio': 'Testeamos que aca haya una descripcion',
            'password': 'Aa1235468!',
        }
        form = SignUpFormUser(data=data)
        self.assertTrue(form.is_valid())

    def test_SignUpUserForm_false(self):
        data = {
            'username': 'TestDeUsuario',
            'firstName': 'Usuario',
            'lastName': 'Para Testear',
            'email': 'esteesunmail@mail.com',
            'phone': '02613893777',
            'birthday': '2000/05/09',
            'bio': 'Testeamos que aca haya una descripcion',
            'password': 'Aa1235468!',
        }
        form = SignUpFormUser(data=data)
        self.assertFalse(form.is_valid())

    def test_SignInForm_true(self):
        data = {
            'username': 'pedro',
            'password': 'supersecretpasswrd'
        }
        form = SignInForm(data=data)
        self.assertTrue(form.is_valid())

    def test_SignInForm_false(self):
        data = {
            'username': 'asldkajsdljaksdlaksjd',
            'password': 32131351
        }
        form = SignInForm(data=data)
        self.assertFalse(form.is_valid())
