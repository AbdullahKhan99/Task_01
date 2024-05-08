# from .serializers import SignUpSerializer
from .serializers import UserSerializer, SignInSerializer
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
        

class SignInView(APIView):
    def post(self,request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                "message":"SignIn Successful",
                "email":serializer.data.get('email'),
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            print(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)