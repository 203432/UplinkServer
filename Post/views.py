from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions

#Importar modelos
from Post.models import Post


#Importar serializadores
from Post.serializers import PostSerializer, PostSerializer2


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

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'text'
    
class PostDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return 0
        
    def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        serializer = PostSerializer2(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        imagen = self.get_object(pk)
        if imagen != 0:
            imagen.delete()
            return Response("Dato eliminado",status=status.HTTP_204_NO_CONTENT)
        return Response("Dato no encontrado",status = status.HTTP_400_BAD_REQUEST) 
    
class UpdateLikesAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.num_likes += 1  # Incrementa el número de likes en uno
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
