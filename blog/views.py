from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets, views, status
from rest_framework.response import Response
# from rest_framework import mixins
# from .models import *
from .documents import *
from .serializers import *
from elasticsearch_dsl import Q, Search

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = UserDocument.search().execute()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        user_data = request.data
        user = UserDocument(**user_data)
        user.save()
        return Response(UserSerializer(user).data)

class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        categories = CategoryDocument.search().execute()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        category_data = request.data
        category = CategoryDocument(**category_data)
        category.save()
        return Response(CategorySerializer(category).data)

class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = ArticleDocument.search().execute()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        article_data = request.data
        article = ArticleDocument(**article_data)
        article.save()
        return Response(ArticleSerializer(article).data)



# class UserListCreateView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class CategoryListCreateView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class ArticleListCreateView(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer




# class ArticleListCreateView(generics.GenericAPIView):
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         # بازیابی تمام مقالات
#         search = ArticleDocument.search().execute()
#         articles = [hit.to_dict() for hit in search]
#         return Response(articles)

#     def post(self, request, *args, **kwargs):
#         # ذخیره مقاله در Elasticsearch
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         article = ArticleDocument(**serializer.validated_data)
#         article.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

# class ArticleSearchView(generics.GenericAPIView):
#     serializer_class = ArticleSerializer

#     def get(self, request, *args, **kwargs):
#         query = request.query_params.get('q', None)
#         if query:
#             q = Q('multi_match', query=query, fields=['title', 'content', 'author', 'category'])
#             search = ArticleDocument.search().query(q)
#             results = search.execute()
#             articles = [hit.to_dict() for hit in results]
#             return Response(articles)
#         return Response([])
    
# def search_articles_by_content(content):
#     s = Search(index="articles").query("match", content=content)
#     return s.execute()

# class ArticleSearchView(views.APIView):
#     def get(self, request, *args, **kwargs):
#         content = request.GET.get('content', '')
#         results = search_articles_by_content(content)
#         data = [{"title": hit.title, "content": hit.content} for hit in results]
#         return Response(data)

# class SaveArticleView(views.APIView):
#     def post(self, request, *args, **kwargs):
#         # داده‌های مقاله را از درخواست JSON می‌گیریم
#         title = request.data.get('title')
#         content = request.data.get('content')
#         published_at = request.data.get('published_at')

#         # ایجاد یک instance از ArticleDocument
#         article = ArticleDocument(
#             title=title,
#             content=content,
#             published_at=published_at
#         )
#         article.save()  # ذخیره مقاله در ایندکس Elasticsearch

#         return Response({"message": "Article saved successfully."}, status=status.HTTP_201_CREATED)