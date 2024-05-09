# from .serializers import SignUpSerializer
from .serializers import UserSerializer, SignInSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from django.conf import settings



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
            user = authenticate(email=request.data['email'], password=request.data['password'])
            access_token = AccessToken.for_user(user)

            response = Response({
                "message":"SignIn Successful",
                "email":serializer.data.get('email'),
                "access": str(access_token),
                 
            },status=status.HTTP_200_OK)

            response.set_cookie(key='access_token', value=str(access_token))
            return response
        else:
            print(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignOutView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        response = Response({"message": "Sign-out successful"}, status=status.HTTP_200_OK)
        response.delete_cookie('access_token')
        return response
    

