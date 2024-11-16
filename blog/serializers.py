from rest_framework import serializers
# from django.utils import timezone
from .documents import *
# from .models import *

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(source='meta.id', read_only=True)  
    username = serializers.CharField(max_length=255)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def validate_username(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("باید فقط شامل حروف و اعداد باشد.")
        elif UserDocument.search().query("match", username=value).execute().hits:
            raise serializers.ValidationError("این نام کاربری از پیش وجود دارد.")
        return value

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("فقط باید شامل حروف باشد.")
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("فقط باید شامل حروف باشد.")
        return value
    
    def create(self, validated_data):
        user = UserDocument(**validated_data)
        user.save()
        return user
        # return super().create(validated_data)

    def update(self, instance, validated_data):
        # return super().update(instance, validated_data)
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    id = serializers.CharField(source='meta.id', read_only=True)  
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()

    def validate_name(self, value):
        if CategoryDocument.search().query("match", name=value).execute().hits:
            raise serializers.ValidationError("این نام از پیش وجود دارد.")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("باید حداقل 10 کاراکتر باشد.")
        return value
    
    def create(self, validated_data):
        category = CategoryDocument(**validated_data)
        category.save()
        return category

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
    

class ArticleSerializer(serializers.Serializer):
    id = serializers.CharField(source='meta.id', read_only=True)  
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    category = serializers.CharField(max_length=255)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only = True)

    # def validate_title(self, value):
    #     if ArticleDocument.search().query("match", title=value).execute().hits:
    #         raise serializers.ValidationError("این عنوان از پیش وجود دارد.")
    #     return value

    def validate_content(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("باید حداقل 10 کاراکتر باشد.")
        return value
    
    def create(self, validated_data):
        article = ArticleDocument(**validated_data)
        article.save()
        return article

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
