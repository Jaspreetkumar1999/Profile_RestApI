from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """ Test Api view """
    def get(self,request, format = None):
        """ Return a list of APIView features"""

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'It is similar to traditional django view',
            'gives you the most control over your logic',
            'It mapped mannually to URLS'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})


