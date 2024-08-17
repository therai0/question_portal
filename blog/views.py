from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import BlogModel
from .serializer import Blog_serializer

# Create your views here.

class Blog_views(APIView):

    def get(self,request):
        if BlogModel.objects.exists():
            try:
                data = BlogModel.objects.all()
                serializer_blog = Blog_serializer(data,many=True,context={'request':request})
                print(serializer_blog.data)
                return Response({'data':serializer_blog.data},status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response({"message":"Something went wrong"})
        else:
            return Response({"message":"No data is avialable"},status=status.HTTP_200_OK)