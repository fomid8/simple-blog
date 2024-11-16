from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<str:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('categories/<str:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('articles/', ArticleView.as_view(), name='article-list'),
    path('articles/<str:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]

# urlpatterns = [
#     path('user/', UserListCreateView.as_view(), name='user-list'),
#     path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    
#     path('category/', CategoryListCreateView.as_view(), name='category-list'),
#     path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    
#     path('article/', ArticleListCreateView.as_view(), name='article-list'),
#     path('article/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),
# ]