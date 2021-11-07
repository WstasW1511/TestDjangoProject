from django.contrib import admin
from outlet.models import OutletModel, ProductModel, CategoryModel
# Register your models here.


@admin.register(OutletModel)
class OutletAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    pass