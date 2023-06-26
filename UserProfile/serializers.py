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
    friends = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'profile', 'friends']

    def update(self, instance, validated_data):
        friends_data = validated_data.pop('friends', None)
        instance = super().update(instance, validated_data)
        
        if friends_data is not None:
            instance.friends.set(friends_data)

        return instance