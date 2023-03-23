from django.shortcuts import render
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Post as Post, User, Comment
from rest_framework import status
from .serializer import PostSerializer, CommentSerializer
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from .serializer import LikeSerializer
from .models import Profile

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


class LikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def patch(self,request, *args, **kwargs):
        instance=self.get_object()
        instance.like +=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)




