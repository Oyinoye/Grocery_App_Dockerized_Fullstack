from django.contrib.auth.models import User
from django.test import TestCase


class TestUserModel(TestCase):

    def setUp(self):
        self.data1 = User.objects.create(username='tola', password='password123')

    def test_user_model_entry(self):
        """
        Test User model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, User))
        self.assertEqual(data.username, 'tola')

    
