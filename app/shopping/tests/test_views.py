from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate
from shopping.models import Grocery
from shopping.views import GroceryViewSet
import json


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        self.apifact = APIRequestFactory
        user = User.objects.create(username='Jane')
        grocery_item = Grocery.objects.create(name='Cookies', description='Snack to eat', quantity=4, is_purchased=False, created_by_id=user.id)

        
    def test_create_product(self):
        """
        Test create product with auth requirement
        """
        user = User.objects.get(username='Jane')
        view = GroceryViewSet.as_view({'post': 'list'})
        request = self.factory.post('http://localhost:8000/api/v1/groceries/', data=json.dumps
        ({
            "name": "Spices",
            "quantity": 3,
            "is_purchased": False,
            "description": "for cooking"
        }), content_type='application/json')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_groceries(self):
        """
        Test create grocery item with auth requirement
        """
        user = User.objects.get(username='Jane')
        view = GroceryViewSet.as_view({'get': 'list'})
        request = self.factory.get('http://localhost:8000/api/v1/groceries/')
        force_authenticate(request, user=user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

