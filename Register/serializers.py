from rest_framework import serializers
from django.contrib.auth.models import User

from UserProfile.models import TablaProfile

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name')
        instance.last_name = validate_data.get('last_name')
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        # instance.first_name = validate_data.get('first_name')
        instance.set_password(validate_data.get('password'))
        instance.save()
        
        profile = TablaProfile.objects.create(
            id_user=instance,
            url_image=None,
            description='',
        )
        return instance
    
    def validate_username(self,data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError('Este nombre de usuario ya esta ocupado, porfavor ingrese otro')
        else:
            return data