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


class UserDetailView(views.APIView):

    def get(self, request, pk):
        user = UserDocument.get(id=pk, ignore=404)
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = UserDocument.get(id=pk, ignore=404)
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        # user.username = valid_data['username']
        # user.first_name = valid_data['first_name']
        # user.last_name = valid_data['last_name']
        for field, value in valid_data.items():
            setattr(user, field, value)
        user.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        user = UserDocument.get(id=pk, ignore=404)
        if not user:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class CategoryDetailView(views.APIView):
    def get(self, request, pk):
        category = CategoryDocument.get(id=pk, ignore=404)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = CategoryDocument.get(id=pk, ignore=404)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        category.name = valid_data['name']
        category.description = valid_data['description']
        category.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        category = CategoryDocument.get(id=pk, ignore=404)
        if not category:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleView(views.APIView):

    def get(self, request):
        articles = ArticleDocument.search().execute()
        serializer = ArticleSerializer(articles, many=True)
        # for hit in articles.hits:
        #     print("Document ID:", hit.meta.id)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        article = ArticleDocument(**valid_data)
        article.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleDetailView(views.APIView):

    def get(self, request, pk):
        # search = ArticleDocument.search().query("term", _id=pk).execute()
        # if not search.hits:
        #     return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        # article = search.hits[0]
        article = ArticleDocument.get(id=pk, ignore=404)
        if not article:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = ArticleDocument.get(id=pk, ignore=404)
        if not article:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        for field, value in valid_data.items():
            setattr(article, field, value)
        # article.created_at = datetime.now().date()
        article.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        article = ArticleDocument.get(id=pk, ignore=404)
        if not article:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

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