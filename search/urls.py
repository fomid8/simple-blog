from django.urls import path
from search.views import *

urlpatterns = [
    path("user/<str:query>/", SearchUsers.as_view()),
    path("category/<str:query>/", SearchCategories.as_view()),
    path("article/<str:query>/", SearchArticles.as_view()),
    path("article/author/<str:query>/", SearchArticlesByAuthor.as_view()),
    path("article/content/<str:query>/", SearchArticlesByContent.as_view()),
]