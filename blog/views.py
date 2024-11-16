from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets, views, status
from rest_framework.response import Response
# from rest_framework import mixins
# from .models import *
from .documents import *
from .serializers import *
from elasticsearch_dsl import Q, Search

class UserView(views.APIView):

    def get(self, request):
        users = UserDocument.search().execute()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        user = UserDocument(**valid_data)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryView(views.APIView):

    def get(self, request):
        categories = CategoryDocument.search().execute()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        category = CategoryDocument(**valid_data)
        category.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleView(views.APIView):
    def get(self, request):
        articles = ArticleDocument.search().execute()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        article = ArticleDocument(**valid_data)
        article.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)



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