
from rest_framework import viewsets
from .serializers import GrocerySerializer
from .models import Grocery
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rideco.auth import CustomAuth
# ViewSets define the view behavior.

#Adjusted to look into jwt auth

class GroceryViewSet(viewsets.ModelViewSet):
    queryset = Grocery.objects.all()
    serializer_class = GrocerySerializer
    authentication_classes = [CustomAuth]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_superuser or self.request.user.is_staff:
            return qs
        return qs.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
