from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator, ValidationError
from django.contrib.auth import authenticate

# class SignUpSerializer(serializers.ModelSerializer):
#     # username = serializers.CharField(max_length=100)
#     # first_name = serializers.CharField(max_length=100,required=True)
#     # last_name = serializers.CharField(max_length=100)
#     email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
#     password = serializers.CharField(min_length=8,write_only=True,required=True)

     
#     class Meta:
#         model= User
#         fields=['username','first_name','last_name','email','password']

#         def validate(self,attrs):
#             print("\n +++++++++++++++++++ \nTHIS IS THE VALIDATE METHOD \n+++++++++++++++++++\n")
#             email_exists = User.objects.filter(email=attrs['email']).exists()
#             if email_exists:
#                 raise ValidationError("User with this email has already been registered")
#             return super().validate(attrs)
        
# #         # def create(self,validated_data):
# #         #     password = validated_data.pop("password")
# #         #     user = super().create(validated_data)
# #         #     user.set_password(password, algorithm='default')

# #         #     user.save()
# #         #     return user
        
#         def create(self, validated_data):
#             print("\n +++++++++++++++++++ \nTHIS IS THE CREATE METHOD \n+++++++++++++++++++\n")            
#             user = User.objects.create(
#                 username=validated_data['username'],
#                 email=validated_data['email'],
#                 first_name=validated_data['first_name'],
#                 last_name=validated_data['last_name']
#             )

            
# #             user.set_password(validated_data['password'])
# #             user.save()
# #             print("USER_PASSWORD: ", user.password)

# #             return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)

        return user
    
class SignInSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        print('hellooo',attrs)

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Failed to login with provided credentials")
            else:
                return attrs
        else:
            raise serializers.ValidationError("Please provide both email and password")

