from django.shortcuts import render
# from .serializers import SignUpSerializer
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SignUpView(APIView):
    def post(self,request):
        # serializer = SignUpSerializer(data=request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = {
                "message":"User Created Successfully",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
    