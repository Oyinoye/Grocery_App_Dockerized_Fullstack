from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase

from shopping.models import Grocery



class TestViewResponses(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        user=User.objects.create(username='admin')
        Grocery.objects.create(name='Biscuits', description='Snack to eat', quantity=5, is_purchased=False, created_by_id=user.id)


    def test_user_registration_url(self):
        """
        Test for successful registration and addition to database
        """
        response = self.c.post('http://localhost:8000/api/v1/users/', {"username": "Jim", "password": "12345678"}, format='json')
        self.assertEqual(response.status_code, 201)

    