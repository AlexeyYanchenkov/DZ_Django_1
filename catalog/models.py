from django.db import models
from django.conf import settings


NULLABLE = {"blank": True, "null": True}


class Product(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара",
    )
    description = models.TextField(
        verbose_name="Описание товара", help_text="Введите описание товара", **NULLABLE
    )
    image = models.ImageField(
        upload_to="catalog/image",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
        **NULLABLE
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Укажите категорию", **NULLABLE
    )
    price = models.IntegerField(
        verbose_name="Цена", help_text="Укажите цену", **NULLABLE
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='products'
    )
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "price"]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name