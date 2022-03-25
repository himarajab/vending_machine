from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer

User=get_user_model()

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )

