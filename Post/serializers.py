from dataclasses import field
from rest_framework import routers, serializers, viewsets


from Post.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')