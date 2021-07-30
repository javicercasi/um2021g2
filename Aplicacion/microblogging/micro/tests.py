from django.test import Client
from .forms import SignUpFormUser
from .models import UserModel
from django.test import TestCase


# Create your tests here.
class SimpleTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
            'first_name': 'Pedro',
            'last_name': 'Carlos',
            'birthday': '2021-07-29'}
        UserModel.objects.create_user(**self.credentials)

    def test_home_GET_login_status_OK(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_home_GET_no_authenticated(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_login_GET_status_OK(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_signup_GET_status_OK(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_SignUpUserForm_true(self):
        data = {
            'username': 'TestDeUsuario',
            'first_name': 'Usuario',
            'last_name': 'Para Testear',
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
            'first_name': 'Usuario',
            'last_name': 'Para Testear',
            'email': 'esteesunmail@mail.com',
            'phone': '02613893777',
            'birthday': '2000/05/09',
            'bio': 'Testeamos que aca haya una descripcion',
            'password': 'Aa1235468!',
        }
        form = SignUpFormUser(data=data)
        self.assertFalse(form.is_valid())
