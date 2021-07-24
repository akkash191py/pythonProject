from rest_framework import serializers
from .models import MyProfile

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = MyProfile
        fields = '__all__'