from django.db import models
from django.contrib.auth.models import Group
from globartigos.apps.base.base_model import BaseModel
from django.utils.translation import gettext_lazy as _


class CategoriesModel(BaseModel):
    name = models.CharField(_("Name"), max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class ArticlesModel(BaseModel):
    title = models.CharField(_("Title"), max_length=255, null=False, blank=False)
    banner = models.ImageField(
        _("Banner"), upload_to="media/articles", null=True, blank=True
    )
    is_highlighted = models.BooleanField(_("Is highlighted"), default=False)
    access_count = models.IntegerField(_("Access Count"), default=0)
    access_control = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Access Control"),
    )
    content = models.TextField(_("Content"), null=False, blank=False)
    category = models.ForeignKey(
        CategoriesModel,
        verbose_name=_("Categories"),
        related_name="articles",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def register_access(self):
        self.access_count += 1
        self.save()

    @property
    def banner_url(self):
        if self.banner:
            return self.banner.url
        return "/static/images/no-image.webp"

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
