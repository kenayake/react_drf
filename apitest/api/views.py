from django.shortcuts import render
from .serializer import *
from rest_framework import viewsets
from .models import *
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class ProdiViewSet(viewsets.ModelViewSet):
    queryset = Prodi.objects.all()
    serializer_class = ProdiSerializer
class MahasiswaViewSet(viewsets.ModelViewSet):
    queryset = Mahasiswa.objects.all()
    serializer_class = MahasiswaSerializer

# Create your views here.
