from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields, Text, Date, Keyword, Nested
from django_elasticsearch_dsl.registries import registry
from .models import *
import datetime


@registry.register_document
class UserDocument(Document):
    id = Keyword(required=True)
    # id = fields.IntegerField()
    username = Text()
    first_name = Text()
    last_name = Text()

    class Index:
        name = 'users'
    
    class Django:
        model = User

# UserDocument.init()

@registry.register_document
class CategoryDocument(Document):
    name = Text()
    description = Text()

    class Index:
        name = 'categories' 

    class Django:
        model = Category 

# CategoryDocument.init()

@registry.register_document
class ArticleDocument(Document):
    title = Text()
    content = Text()
    author = Nested(UserDocument)
    category = Nested(CategoryDocument)
    created_at = Date()

    class Index:
        name = 'articles'
    
    class Django:
        model = Article

    def save(self, **kwargs):
        self.created_at = self.created_at or datetime.now()
        return super().save(**kwargs)


# @registry.register_document
# class ArticleDocument(Document):
#     author = fields.ObjectField(properties={
#         "id": fields.IntegerField(),
#         "first_name": fields.TextField(),
#         "last_name": fields.TextField(),
#         "username": fields.TextField(),
#     })
#     categories = fields.ObjectField(properties={
#         "id": fields.IntegerField(),
#         "name": fields.TextField(),
#         "description": fields.TextField(),
#     })
#     type = fields.TextField(attr="type_to_string")

#     class Index:
#         name = "articles"
#         settings = {
#             "number_of_shards": 1,
#             "number_of_replicas": 0,
#         }

#     class Django:
#         model = Article
#         fields = [
#             "title",
#             "content",
#             "created_datetime",
#             "updated_datetime",
#         ]


