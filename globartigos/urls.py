from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from globartigos.home import HomeView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name="home"),
    path("articles/", include("globartigos.apps.article.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
