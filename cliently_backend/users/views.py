from rest_framework import generics
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import AllowAny


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]