
from django.http import FileResponse,Http404
from  rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HomePage_logo
from .serialzer import Home_page_serializer
import os
from django.conf import settings
import base64

# Create your views here.

class Homepage_logo_view(APIView):
        
    def get(self, request):
        images = HomePage_logo.objects.all()
        serializer = Home_page_serializer(images, many=True, context={'request': request})
        return Response(serializer.data)

    

       