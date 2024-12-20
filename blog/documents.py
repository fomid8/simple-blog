from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields, Text, Date, Keyword, Nested
from django_elasticsearch_dsl.registries import registry
from .models import *
from datetime import datetime 


@registry.register_document
class UserDocument(Document):
    # id = fields.IntegerField()
    username = fields.TextField()
    first_name = fields.TextField()
    last_name = fields.TextField()

    class Index:
        name = 'users'
    
    class Django:
        model = User

    def save(self, **kwargs):
        return super().save(**kwargs)

# UserDocument.init()

@registry.register_document
class CategoryDocument(Document):
    name = fields.TextField()
    description = fields.TextField()

    class Index:
        name = 'categories' 

    class Django:
        model = Category 
    
    def save(self, **kwargs):
        return super().save(**kwargs)

# CategoryDocument.init()

@registry.register_document
class ArticleDocument(Document):
    title = fields.TextField()
    content = fields.TextField()
    author = fields.TextField() 
    category = fields.TextField() 
    created_at = fields.DateField()

    class Index:
        name = 'articles'
    
    class Django:
        model = Article

    def save(self, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now()
        return super().save(**kwargs)
