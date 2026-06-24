from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


class CorrectTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    #authentication_classes = [JWTAuthentication, users.authentication.BotAuthentication]


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_me(request):
    user = request.user
    username = user.username
    email = user.email
    is_staff = user.is_staff
    is_superuser = user.is_superuser

    results = {
        'username' : username,
        'email' : email,
        'is_staff' : is_staff,
        'is_superuser' : is_superuser
    }

    return Response(results)
