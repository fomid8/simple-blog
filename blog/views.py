# from django.shortcuts import render
from rest_framework import viewsets, views, status
from rest_framework.response import Response
# from rest_framework import mixins
# from .models import *
from .documents import *
from .serializers import *
# from elasticsearch_dsl import Q, Search


class UserView(views.APIView):

    def get(self, request):
        users = UserDocument.search().execute()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.create(serializer.validated_data)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


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
        updated_user = serializer.update(user, serializer.validated_data)
        return Response(UserSerializer(updated_user).data)

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
        category = serializer.create(serializer.validated_data)
        return Response(CategorySerializer(category).date, status=status.HTTP_201_CREATED)


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
        updated_category = serializer.update(category, serializer.validated_data)
        return Response(CategorySerializer(updated_category).data)

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
        article = serializer.create(serializer.validated_data)
        return Response(ArticleSerializer(article).data, status=status.HTTP_201_CREATED)


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
        updated_article = serializer.update(article, serializer.validated_data)
        # article.created_at = datetime.now().date()
        return Response(ArticleSerializer(updated_article).data)


    def delete(self, request, pk):
        article = ArticleDocument.get(id=pk, ignore=404)
        if not article:
            return Response({"error": "Article not found"}, status=status.HTTP_404_NOT_FOUND)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



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