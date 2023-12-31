from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        first_name=validated_data['first_name']
        last_name=validated_data['last_name']
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=validated_data['email'],
            password=validated_data['password'],
            username=f"{first_name} {last_name}"
        )
        return user

    class Meta:
        model = User 
        fields = ['url', 'email','first_name','last_name','password']
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

