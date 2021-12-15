from rest_framework import serializers
from django.contrib.auth.models import User


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email',
                  'is_staff', 'first_name', 'last_name']


class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email',
                  'is_staff', 'first_name', 'last_name', 'password']
