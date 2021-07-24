from django.urls import path
from .api import UserCreateApi, UserApi, UserUpdateApi, UserDeleteApi

urlpatterns = [
    path('api/create', UserCreateApi.as_view()),
    path('api', UserApi.as_view()),
    path('api/<int:pk>', UserUpdateApi.as_view()),
    path('api/<int:pk>/delete', UserDeleteApi.as_view()),
]