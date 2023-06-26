from django.shortcuts import render

# Create your views here.
from multiprocessing import context
from webbrowser import get
from django.shortcuts import render
from UserProfile.serializers import TablaProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import exceptions

import os.path
from .serializers import UserSerializer
from pathlib import Path

from django.contrib.auth.models import User
from UserProfile.models import TablaProfile
from UserProfile.serializers import TablaProfileSerializer

# Create your views here.
class TablaProfileList(APIView):
    def get_objectUser(self, idUser):
      try:
        return User.objects.get(pk = idUser)
      except User.DoesNotExist:
        return 404
    

    def post(self, request):
        archivos = request.data['url_image']
        serializer = TablaProfileSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el modelo
            image = TablaProfile(**validated_data)
            image.save()
            serializer_response = TablaProfileSerializer(image)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response("Este usuario ya tiene un perfil")
    

class Friends(APIView):
    def get_object(self, pk):
        try:
            return TablaProfile.objects.get(id_user = pk)
        except TablaProfile.DoesNotExist:
            return 404
    def res_custom(self, user, data, status):
        response = {
            "friends": data.get('friends'),
        }
        return response

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            idResponse = TablaProfileSerializer(idResponse)
            user = User.objects.filter(id=pk).values()
            responseOK = self.res_custom(user,idResponse.data,status.HTTP_200_OK)
            return Response(responseOK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        try:
            profile = TablaProfile.objects.get(id_user=pk)
        except TablaProfile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        friend_ids = request.data.get('friend_ids', [])

        # Convertir los IDs de los amigos en objetos User
        friends = []
        for friend_id in friend_ids:
            try:
                friend = User.objects.get(pk=friend_id)
                friends.append(friend)
            except User.DoesNotExist:
                pass

        # Agregar los amigos a la lista friends del perfil
        profile.friends.set(friends)

        return Response(status=status.HTTP_200_OK)

class TablaProfileDetail(APIView):
    def get_object(self, pk):
        try:
            return TablaProfile.objects.get(id_user = pk)
        except TablaProfile.DoesNotExist:
            return 404
    def res_custom(self, user, data, status):
        response = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email'],
            "id_user" : data.get('id_user'),
            "id_profile": data.get('id'),
            "url_image" : data.get('url_image'),
            "description": data.get('description'),
            "status" : status
        }
        return response

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            idResponse = TablaProfileSerializer(idResponse)
            user = User.objects.filter(id=pk).values()
            responseOK = self.res_custom(user,idResponse.data,status.HTTP_200_OK)
            return Response(responseOK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        archivos = request.data['url_image']
        idResponse = self.get_object(pk)
        if(idResponse != 404):
            serializer = TablaProfileSerializer(idResponse)
            try:
                os.remove('assets/'+str(idResponse.url_image))
            except os.error:
                print("La imagen no existe")
            idResponse.url_image = archivos
            idResponse.save()
            return Response("Todo kul",status.HTTP_201_CREATED)
        else:
            return Response("No salio bien")
        
        
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
    
class UserDetailAPIView2(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

class ProfileUser(APIView):
    
    def res_custom(self, user, status):
        response = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email'],
            "status" : status
        }
        return response;
    
    def get(self, request, pk, format=None):
        idResponse = User.objects.filter(id=pk).values()
        if(idResponse != 404):
            responseData = self.res_custom(idResponse, status.HTTP_200_OK)
            return Response(responseData)
        return("No se encontró el usuario")
    
    def put(self, request, pk, format=None):
        data = request.data
        user = User.objects.filter(id = pk)
        user.update(username = data.get('username'))
        user.update(first_name = data.get('first_name'))
        user.update(last_name = data.get('last_name'))
        user.update(email = data.get('email'))
        user2 = User.objects.filter(id=pk).values()
        return Response(self.res_custom(user2, status.HTTP_200_OK))
    
        