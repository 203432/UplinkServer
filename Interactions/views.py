from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import permissions
from Interactions.models import Comments
from Interactions.serializers import CommentsSerializer

# Create your views here.
class CommentsList(ListAPIView):
    def get(self,request,format=None):
        queryset=Comments.objects.all()
        serializer = CommentsSerializer(queryset,many=True,context={'request':request})

        
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=CommentsSerializer(data=request.data)
        if serializer.is_valid():
            # asignar el usuario autenticado a la instancia de Post
            serializer.save(user=request.user)
            serializer_response = serializer.data
            return Response(serializer_response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CommentDetail(APIView):
    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            return 0
        
    def get(self, request, pk, format = None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse  = CommentsSerializer(idResponse)
            return Response(idResponse.data, status=status.HTTP_200_OK)
        return Response("No se encontro el dato", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        serializer = CommentsSerializer(idResponse, data = request.data)
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
    
class CommentListByPost(ListAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        postP = self.kwargs['post']
        queryset = Comments.objects.filter(post=postP)
        return queryset