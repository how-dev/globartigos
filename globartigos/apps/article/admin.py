from django.contrib import admin
from django.utils.html import mark_safe

from globartigos.apps.article.models import CategoriesModel, ArticlesModel


class ActivateMixin:
    def activate(self, _request, queryset):
        queryset.update(is_active=True)

    activate.short_description = "Ativar"

    def deactivate(self, _request, queryset):
        queryset.update(is_active=False)

    deactivate.short_description = "Desativar"


@admin.register(CategoriesModel)
class CategoriesAdmin(ActivateMixin, admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)
    date_hierarchy = "created_at"
    list_per_page = 10
    actions = ["activate", "deactivate"]


@admin.register(ArticlesModel)
class ArticlesAdmin(ActivateMixin, admin.ModelAdmin):
    list_display = (
        "banner_preview",
        "title",
        "created_at",
        "updated_at",
        "is_active",
        "is_highlighted",
        "access_count",
        "category",
    )
    search_fields = ("title", "content")
    list_filter = ("is_active", "is_highlighted", "category")
    date_hierarchy = "created_at"
    list_per_page = 10
    actions = ["make_highlight", "activate", "deactivate"]
    readonly_fields = ("access_count",)
    list_display_links = ("title",)

    def make_highlight(self, _request, queryset):
        queryset.update(is_active=True, is_highlighted=True)

    make_highlight.short_description = "Destacar artigo"

    @staticmethod
    def banner_preview(obj):
        html = f'<img src="{obj.banner_url}" width="100px" />'

        return mark_safe(html)
