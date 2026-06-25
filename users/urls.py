from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import  CorrectTokenObtainPairView, get_me, ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('profile', ProfileViewSet)

urlpatterns = [
    path("auth/login/", CorrectTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('get_me/', get_me),
    path('', include(router.urls))
]