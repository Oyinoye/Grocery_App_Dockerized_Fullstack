from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase

from shopping.models import Grocery


class TestGroceryModel(TestCase):

    """
    Test Grocery model instantiation and relationship
    """

    def setUp(self):
        user = User.objects.create(username='app', password="app12345")
        self.data1 = Grocery.objects.create(name='Biscuits', description='Snack to eat', quantity=5, is_purchased=False, created_by_id=user.id)

    def test_Grocery_model_entry(self):
        """
        Test Grocery model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Grocery))
        self.assertEqual(data.name, 'Biscuits')

    