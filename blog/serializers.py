from rest_framework import serializers
# from .models import *
# blog_project/blog/serializers.py

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    author = UserSerializer(many= True)
    category = CategorySerializer(many= True)
    content = serializers.CharField()
    created_at = serializers.DateField()