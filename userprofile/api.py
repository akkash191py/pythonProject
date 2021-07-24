from rest_framework import generics
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import MyProfile


class UserCreateApi(generics.CreateAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = UserSerializer


class UserApi(generics.ListAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = UserSerializer


class UserUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = UserSerializer

class UserDeleteApi(generics.DestroyAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = UserSerializer