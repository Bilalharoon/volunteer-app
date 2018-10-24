from rest_framework import serializers
from .models import LoginUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields = '__all__'