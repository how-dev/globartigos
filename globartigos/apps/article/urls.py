from django.urls import path

from .views import ArticleListView, ArticleDetailView

app_name = "article"

urlpatterns = [
    path("", ArticleListView.as_view(), name="articles-list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="articles-detail"),
]
