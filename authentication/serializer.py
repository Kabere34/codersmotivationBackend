from django.conf import settings
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from authentication.models import AbstractUser
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from authentication.models import User


# class UserRegistrationSerializer(RegisterSerializer):
#   class Meta:
#     model = settings.AUTH_USER_MODEL
#     fields=('username','email','password','password2')

# def get_cleaned_data(self):
#   data=super(UserRegistrationSerializer,self).get_cleaned_data()
#   return data

# def save(self, request):
#   user=super(UserRegistrationSerializer)
#   user.save()
#   return user

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)






