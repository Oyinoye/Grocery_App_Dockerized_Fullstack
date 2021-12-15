
from rest_framework import viewsets
from .serializers import UserSerializer, CreateUserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    create_serializer_class = CreateUserSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action != 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.create_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        usr = self.perform_create(serializer)
        read_serializer = self.serializer_class(
            instance=usr, context={'request': request})
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password'))
        user.is_active = True
        user.save()
        return user
