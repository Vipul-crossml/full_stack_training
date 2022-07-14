import email
from urllib import response
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import *
# Create your views here.
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


class Registeruser(APIView):
    """
    wsad
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong'})
            
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({'status': 200, 'payload': serializer.data,  'refresh': str(refresh), 'access': str(refresh.access_token), 'message': 'user registration success'})

from django.contrib.auth import authenticate, login

@api_view(["POST"])
@permission_classes([AllowAny])

def login_user(request):
    username = request.POST['email']
    print(username)
    password = request.POST['password']
    print(password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'status': 200,})
        # Redirect to a success page.
        ...
    else:
        return Response({'status': 404,})