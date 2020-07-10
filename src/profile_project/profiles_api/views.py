from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class HelloApiView(APIView):
    """ Test Api view """
    serializer_class = HelloSerializer


    def get(self,request, format = None):
        """ Return a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to traditional django view',
            'gives you the most control over your logic',
            'It mapped mannually to URLS'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})


    def post(self,request):
        """Create  a hello message with our name """
        serializer = HelloSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else :
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """handles updating an object"""

        return Response({"method": "put"})

    def patch(self, request, pk=None):
        """ Patch request, only update fields provided in the request  """

        return Response({"method":"patch"})

    def delete(self, request, pk=None):
        """ Delete"""
        return Response({"method":"delete"})



class HelloViewSet(viewsets.ViewSet) :
    """ Test API ViewSet  """

    def list(self,request):
        """ Return hello message"""

        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code' ]
        return Response ({'message': 'hello', 'a_viewset': a_viewset})





