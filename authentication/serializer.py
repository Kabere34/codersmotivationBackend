from django.conf import settings
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from authentication.models import AbstractUser, Driver
from django.contrib.auth import authenticate
from rest_framework.response import Response


class UserRegistrationSerializer(RegisterSerializer)
  class Meta:
    model = settings.AUTH_USER_MODEL
    fields=('username','email','password','password2')

def get_cleaned_data(self):
  data=super(UserRegistrationSerializer,self).get_cleaned_data()
  return data

def save(self, request):
  user=super(UserRegistrationSerializer)
  user.save()
  return user


class LoginSerialzer(serializers.Serializer):
  username = serializers.CharField(max_length=50)
  password = serializers.CharField(max_length=50)




