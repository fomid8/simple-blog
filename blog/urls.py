from django.urls import path, include
from .views import *
# from rest_framework import routers


urlpatterns = [
    path('user/', UserListCreateView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    
    path('category/', CategoryListCreateView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    
    path('article/', ArticleListCreateView.as_view(), name='article-list'),
    path('article/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-detail'),
]

# router = routers.DefaultRouter()
# router.register(r"user", UserView)
# router.register(r"category", CategoryView)
# router.register(r"article", ArticleView)

# urlpatterns = [
#     path("", include(router.urls)),
# ]