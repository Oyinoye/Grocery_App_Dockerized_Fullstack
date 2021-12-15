from rest_framework import serializers
from .models import Grocery


# Serializers define the API representation.
class GrocerySerializer(serializers.HyperlinkedModelSerializer):
    quantity = serializers.IntegerField()

    class Meta:
        model = Grocery
        fields = ['quantity', 'url', 'name',
                  'description', 'created_at', 'updated_at']
