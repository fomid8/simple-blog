from django.shortcuts import render
import abc
from rest_framework.response import Response
from elasticsearch_dsl import Q
from rest_framework import views
from rest_framework.pagination import LimitOffsetPagination
from blog.documents import ArticleDocument, UserDocument, CategoryDocument
from blog.serializers import ArticleSerializer, UserSerializer, CategorySerializer
import re
import unicodedata


class PaginatedElasticSearchAPIView(views.APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden
        and return a Q() expression."""

    def preprocess_query(self, query):
        # remove extra spaces
        query = query.strip()
        # query = query.lower()
        query = unicodedata.normalize('NFKC', query)
        # remove extra characters
        query = re.sub(r'[^\w\s]', '', query)
        return query

    def get(self, request, query):
        try:
            preprocessed_query = self.preprocess_query(query)
            q = self.generate_q_expression(preprocessed_query)
            search = self.document_class.search().query(q)
            response = search.execute()
            print(f"Found {response.hits.total.value} hit(s) for query: '{query}'")
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class SearchUsers(PaginatedElasticSearchAPIView):
    serializer_class = UserSerializer
    document_class = UserDocument

    def generate_q_expression(self, query):
        return Q("bool",
                 should=[
                     Q("match", username=query),
                     Q("match", first_name=query),
                     Q("match", last_name=query),
                     # Ngram
                     Q("query_string", query=f"*{query}*", fields=["username^2", "first_name^1", "last_name^1"])
                 ], minimum_should_match=1)


class SearchCategories(PaginatedElasticSearchAPIView):
    serializer_class = CategorySerializer
    document_class = CategoryDocument

    def generate_q_expression(self, query):
        return Q(
                "multi_match", query=query,
                fields=[
                    "name",
                    "description",
                ], fuzziness="auto")


class SearchArticles(PaginatedElasticSearchAPIView):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def generate_q_expression(self, query):
        return Q(
                "multi_match", query=query,
                fields=[
                    "title",
                    "category"
                ], fuzziness="auto")


class SearchArticlesByAuthor(PaginatedElasticSearchAPIView):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def generate_q_expression(self, query):
        return Q("match", author=query)


class SearchArticlesByContent(PaginatedElasticSearchAPIView):
    serializer_class = ArticleSerializer
    document_class = ArticleDocument

    def generate_q_expression(self, query):
        return Q("multi_match", query=query,
                fields=["content"],
                fuzziness="auto")