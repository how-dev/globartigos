from unittest.mock import patch

from django.test import TestCase
from django.db import models
from .models import ArticlesModel, CategoriesModel
from globartigos.apps.base.base_model import BaseModel


class TestArticleModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = ArticlesModel

    def test_parent_model(self):
        self.assertTrue(issubclass(ArticlesModel, BaseModel))

    def test_title_field(self):
        field = self.model._meta.get_field("title")

        self.assertEqual(field.verbose_name, "Title")
        self.assertEqual(field.max_length, 255)
        self.assertFalse(field.null)
        self.assertFalse(field.blank)
        self.assertTrue(isinstance(field, models.CharField))

    def test_banner_field(self):
        field = self.model._meta.get_field("banner")

        self.assertEqual(field.verbose_name, "Banner")
        self.assertEqual(field.upload_to, "media/articles")
        self.assertTrue(field.null)
        self.assertTrue(field.blank)
        self.assertTrue(isinstance(field, models.ImageField))

    def test_is_highlighted_field(self):
        field = self.model._meta.get_field("is_highlighted")

        self.assertEqual(field.verbose_name, "Is highlighted")
        self.assertFalse(field.default)
        self.assertTrue(isinstance(field, models.BooleanField))

    def test_access_count_field(self):
        field = self.model._meta.get_field("access_count")

        self.assertEqual(field.verbose_name, "Access Count")
        self.assertEqual(field.default, 0)
        self.assertTrue(isinstance(field, models.IntegerField))

    def test_access_control_field(self):
        field = self.model._meta.get_field("access_control")

        self.assertEqual(field.verbose_name, "Access Control")
        self.assertTrue(field.null)
        self.assertTrue(field.blank)
        self.assertTrue(isinstance(field, models.ForeignKey))

    def test_content_field(self):
        field = self.model._meta.get_field("content")

        self.assertEqual(field.verbose_name, "Content")
        self.assertFalse(field.null)
        self.assertFalse(field.blank)
        self.assertTrue(isinstance(field, models.TextField))

    def test_category_field(self):
        field = self.model._meta.get_field("category")

        self.assertEqual(field.verbose_name, "Categories")
        self.assertEqual(field.remote_field.related_name, "articles")
        self.assertTrue(isinstance(field, models.ForeignKey))
        self.assertEqual(field.remote_field.model, CategoriesModel)

    def test_str_method(self):
        instance = self.model(title="Test")
        self.assertEqual(str(instance), "Test")

    @patch.object(ArticlesModel, "save")
    def test_register_access_method(self, mock_save):
        instance = self.model(access_count=0)
        instance.register_access()
        self.assertEqual(instance.access_count, 1)

        mock_save.assert_called_once_with()

    def test_banner_url_property(self):
        instance = self.model(banner=None)
        self.assertEqual(instance.banner_url, "/static/images/no-image.webp")

        instance = self.model(banner="test")
        self.assertEqual(instance.banner_url, "/test")

    def test_meta_verbose_name(self):
        self.assertEqual(self.model._meta.verbose_name, "Article")
        self.assertEqual(self.model._meta.verbose_name_plural, "Articles")


class TestCategoriesModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model = CategoriesModel

    def test_parent_model(self):
        self.assertTrue(issubclass(CategoriesModel, BaseModel))

    def test_name_field(self):
        field = self.model._meta.get_field("name")

        self.assertEqual(field.verbose_name, "Name")
        self.assertEqual(field.max_length, 255)
        self.assertFalse(field.null)
        self.assertFalse(field.blank)
        self.assertTrue(isinstance(field, models.CharField))

    def test_str_method(self):
        instance = self.model(name="Test")
        self.assertEqual(str(instance), "Test")

    def test_meta_verbose_name(self):
        self.assertEqual(self.model._meta.verbose_name, "Category")
        self.assertEqual(self.model._meta.verbose_name_plural, "Categories")
