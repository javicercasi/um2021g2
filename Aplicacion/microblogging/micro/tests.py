from django.test import TestCase, Client


# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_signin_status_OK(self):
        response = self.client.get('/signin/')
        self.assertEqual(response.status_code, 200)

    def test_home_status_OK(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_signin_POST_no_existe(self):
        response = self.client.post('/signin/', {'username': 'hola', 'password': 'chau'})
        self.assertEqual(response.status_code, 400)
        # self.assertContains(response.content, '')
