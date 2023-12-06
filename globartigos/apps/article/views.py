from django.views.generic import ListView, DetailView
from django.db.models import Q

from .utils import ArticleViewMixin


class ArticleListView(ArticleViewMixin, ListView):
    template_name = "articles/list.html"
    paginate_by = 10
    extra_context = {
        "search": None,
        "category": None,
        "paginate_by": None,
        "object_count": None,
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        queryset = self._filter_by_category(queryset, request)
        queryset = self._filter_by_search(queryset, request)
        self.extra_context["object_count"] = queryset.count()
        return queryset

    def _filter_by_search(self, queryset, request):
        search = request.GET.get("search")
        if search:
            self.extra_context["search"] = search
            queryset = queryset.filter(
                Q(title__icontains=search)
                | Q(content__icontains=search)
                | Q(category__name__icontains=search)
                | Q(created_at__icontains=search)
            )
        return queryset

    def _filter_by_category(self, queryset, request):
        category = request.GET.get("category")
        if category:
            self.extra_context["category"] = category
            queryset = queryset.filter(category__name=category)
        return queryset

    def get_paginate_by(self, queryset):
        request = self.request
        paginate_by = request.GET.get("paginate_by", self.paginate_by)
        self.extra_context["paginate_by"] = paginate_by
        return paginate_by


class ArticleDetailView(ArticleViewMixin, DetailView):
    template_name = "articles/detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_active=True)
