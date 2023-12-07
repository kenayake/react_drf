from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        print(validated_data['first_name'])
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=make_password(
                validated_data['password']
            ),
            username=f"{validated_data['first_name']} {validated_data['last_name']}"
        )
        return user

    class Meta:
        model = User
        fields = ['url', 'email','first_name','last_name','password']

class ProdiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prodi
        fields = '__all__'
        
class MahasiswaSerializer(serializers.ModelSerializer):
    prodi = ProdiSerializer(many=False, read_only=True)
    class Meta:
        model = Mahasiswa
        fields = ['name', 'nim', 'prodi', 'image']

