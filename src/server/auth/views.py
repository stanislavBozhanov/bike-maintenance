from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all() # This is not used, but required for the CreateAPIView
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer
