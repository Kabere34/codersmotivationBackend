from django.shortcuts import render
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post as Post
from .models import Profile
from rest_framework import status
from .serializer import PostSerializer, ProfileSerializer

# Create your views here.

def index(request):
    return render(request,"index.html")

class Postapi(APIView):
    def get(self, request, format=None):
        all_post = Post.objects.all()
        serializers = PostSerializer(all_post, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
