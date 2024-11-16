from django.urls import path, include
from .views import *

urlpatterns = [
    path('users/', UserView.as_view(), name='user-list'),
    path('categories/', CategoryView.as_view(), name='category-list'),
    path('articles/', ArticleView.as_view(), name='article-list'),
]

# urlpatterns = [
#     path('user/', UserListCreateView.as_view(), name='user-list'),
#     path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    
#     path('category/', CategoryListCreateView.as_view(), name='category-list'),
#     path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    
#     path('article/', ArticleListCreateView.as_view(), name='article-list'),
#     path('article/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),
# ]