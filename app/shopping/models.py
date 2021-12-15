from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Grocery(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_purchased = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
