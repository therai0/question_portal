from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadFile
from .serializer import Question_serialzer

# Create your views here.

class Question_views(APIView):

    def get(self,request):
        try:
            if UploadFile.objects.exists():
                data = UploadFile.objects.all()
                serializer_data = Question_serialzer(data,many=True,context={'request':request})
                return Response(serializer_data.data,status=status.HTTP_200_OK)
            else:
                return Response([],status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
