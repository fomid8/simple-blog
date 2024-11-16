from rest_framework import serializers
# from django.utils import timezone
from .documents import *
# from .models import *

class UserSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    username = serializers.CharField(max_length=200)
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)

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


class CategorySerializer(serializers.Serializer):
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
    

class ArticleSerializer(serializers.Serializer):
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
