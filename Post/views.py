from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions

#Importar modelos
from Post.models import Post


#Importar serializadores
from Post.serializers import PostSerializer


class PostListByOwner(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        userP = self.kwargs['user']
        queryset = Post.objects.filter(user=userP)
        return queryset

# Create your views here.
class PostList(ListAPIView):
    def get(self,request,format=None):
        queryset=Post.objects.all()
        serializer = PostSerializer(queryset,many=True,context={'request':request})

        
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            # asignar el usuario autenticado a la instancia de Post
            serializer.save(user=request.user)
            serializer_response = serializer.data
            return Response(serializer_response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
