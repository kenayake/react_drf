from django.shortcuts import render
from .serializer import *
from rest_framework import viewsets,views
from rest_framework.response import Response
from .models import *
from django.contrib.auth.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
class LoginAPIView(views.APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user is None:
            return Response({"Error":"No user with that email exist"},status=404)
        else:
            if user.check_password(password):
                return Response(UserSerializer(user, context={'request': request}).data,status=200)
            else:
                return Response({"Error":"Password is incorrect"},status=400)