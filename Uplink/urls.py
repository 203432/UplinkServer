
from django.contrib import admin
from django.urls import path, include
from rest_framework import generics
from Register.serializers import UserSerializer 
from rest_framework.permissions import AllowAny
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
# )

urlpatterns = [
    path('api/v1/login/', include('Login.urls')),
    path('api/v1/post/', include('Post.urls')),
    path('api/v1/register/', generics.CreateAPIView.as_view(
        serializer_class=UserSerializer,
        permission_classes=[AllowAny], # Aquí utilizamos AllowAny para permitir el registro sin autenticación
    )),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]