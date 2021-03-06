from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HelloSerializer,UserProfileSerializer,ProfileFeedItemSerializer
from rest_framework import status
from rest_framework import viewsets
from . import models
from . import permission
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated
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

    serializer_class = HelloSerializer

    def list(self,request):
        """ Return hello message"""

        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code' ]
        return Response ({'message': 'hello', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a new hello message """  

        serializer = HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name') 
            message = f"Hello {name}"
            return Response({"message": message})

        else :
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        """ Handles getting an object by its ID  """

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handles updating an object"""  
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles partial updating an object"""  
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles deleting an object"""  
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
     """ Handles creating,reading and updating profiles """

     serializer_class = UserProfileSerializer
     queryset = models.UserProfile.objects.all()
     authentication_classes = {TokenAuthentication,}
     permission_classes = {permission.UpdateOwnProfile,}
     filter_backends = {filters.SearchFilter,}
     search_fields = {'name','email',}


class LoginViewSet(viewsets.ViewSet):
    """Check email and password and return an auth token """
    serializer_class = AuthTokenSerializer

    def create(self,request):
        """ Uses the ObtainAuthetoken APIView to validate and create a token """
        return ObtainAuthToken().post(request)


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating reading and updating profile feed item"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permission.PostOwnStatus, IsAuthenticated)


    def perform_create(self, serializer):
        """ Set user profile to the logged in user"""
        serializer.save(user_profile= self.request.user)




  
