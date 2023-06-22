from dataclasses import fields
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

# importacion de modelos
from UserProfile.models import TablaProfile



class TablaProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaProfile
        fields = ('__all__')
        

class UserSerializer(serializers.ModelSerializer):
    profile = TablaProfileSerializer(source='tablaprofile', read_only=True)

    class Meta:
        model = User
        fields = ['pk','username', 'email', 'first_name', 'last_name', 'profile']