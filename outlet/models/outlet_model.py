from django.db import models


class OutletModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название магазина')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = "Магазины"

    def __str__(self):
        return str(self.name)


class ProductModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.CharField(max_length=250, verbose_name='Описание товара')
    category = models.ForeignKey('outlet.CategoryModel', related_name='products', on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return str(self.title)


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')
    description = models.CharField(max_length=255, verbose_name='Описание категории', blank=True, null=True)
    outlet = models.ForeignKey(OutletModel, related_name='categories', on_delete=models.CASCADE, verbose_name='Магазин')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return str(self.name)




