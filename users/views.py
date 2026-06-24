from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .models import Profile
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import ProfileSerializer


class CorrectTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    #authentication_classes = [JWTAuthentication, users.authentication.BotAuthentication]



class ProfileViewSet(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_me(request):
    user = request.user
    profile = Profile.objects.get(owner=user)
    first_name = profile.first_name
    last_name = profile.last_name
    reputation = profile.reputation

    results = {
        'first_name' : first_name,
        'last_name' : last_name,
        'reputation' : reputation
    }

    return Response(results)
