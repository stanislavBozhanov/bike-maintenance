from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.authtoken.models import Token

class Register(CreateAPIView):
  queryset = User.objects.all() # This is not used, but required for the CreateAPIView
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class Login(APIView):
  def post(self, request):
    data = request.data
    username = data.get('email', None)
    password = data.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
      token, created = Token.objects.get_or_create(user=user)
      return Response({
          'token': token.key,
          'message': 'You have successfully logged in'
        },
        status=status.HTTP_200_OK
      )
    return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
