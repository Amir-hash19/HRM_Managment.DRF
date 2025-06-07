from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone", "similarity"]




class CreateCustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["slug", "is_staff"]




class UserDeleteOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'is_active']
        extra_kwargs = {
            'email':{"required":False},
            'username':{"required":False}
        }




class CreateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["name", "id"]