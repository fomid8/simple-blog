from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"user", UserView)
router.register(r"category", CategoryView)
router.register(r"article", ArticleView)

urlpatterns = [
    path("", include(router.urls)),
]

# urlpatterns = [
#     path('user/', UserView.as_view(), name='user-list'),
#     path('category/', CategoryView.as_view(), name='category-list'),
#     path('article/', ArticleView.as_view(), name='article-list'),
# ]
