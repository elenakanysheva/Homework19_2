from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", **NULLABLE)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", **NULLABLE)
    image = models.ImageField(upload_to="products/", verbose_name="Изображение", **NULLABLE)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Категория",
        related_name='products'
    )
    price = models.IntegerField(verbose_name="Цена", **NULLABLE)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата последнего изменения", auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    def __str__(self):
        return self.name
