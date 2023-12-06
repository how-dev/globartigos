from django.db.models import Q
from django.http import Http404

from .models import ArticlesModel, CategoriesModel


# noinspection PyUnresolvedReferences
class ArticleViewMixin:
    model = ArticlesModel
    ordering = ["-created_at"]
    template_404 = "404.html"
    object = None

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True)

        user = self.request.user

        if user.is_authenticated:
            return queryset.filter(
                Q(access_control__in=user.groups.all()) | Q(access_control__isnull=True)
            )

        return queryset.filter(access_control__isnull=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self._set_categories(context)
        self._set_highlighteds(context)
        self._set_most_read(context)
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return self.render_to_response(
                self.get_context_data(
                    request=request, template_name=self.template_404, status=404
                )
            )

    def get_object(self, *args, **kwargs):
        article = super().get_object(*args, **kwargs)
        if article:
            article.register_access()

        return article

    def _set_most_read(self, context):
        queryset = self.get_queryset()
        context["most_read"] = queryset.order_by("-access_count")[:3]

    def _set_highlighteds(self, context):
        queryset = self.get_queryset()
        context["highlights"] = queryset.filter(is_highlighted=True).order_by(
            "-created_at"
        )

    @staticmethod
    def _set_categories(context):
        context["categories"] = (
            CategoriesModel.objects.filter(is_active=True)
            .distinct()
            .order_by("name")
            .values_list("name", flat=True)
        )
