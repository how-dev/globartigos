from django.views.generic import ListView

from globartigos.apps.article.utils import ArticleViewMixin


class HomeView(ArticleViewMixin, ListView):
    template_name = "home.html"
    paginate_by = 6
