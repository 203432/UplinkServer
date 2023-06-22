from rest_framework import routers, serializers, viewsets


from Interactions.models import Comments
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('__all__')