from rest_framework import serializers
from .models import Post,Comment
from authentication.models import User
from rest_framework.response import Response

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id', 'title','content','likes')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('id', 'author', 'post', 'text','created_at')
        read_only_fields=('id','created_at')

