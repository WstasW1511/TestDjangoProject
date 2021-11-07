from rest_framework.serializers import ModelSerializer
from outlet.models import *
from .product_serializer import ProductListSerializer
# from .outlet_serializer import OutletListSerializer


class CategoryListSerializer(ModelSerializer):
    products = ProductListSerializer(required=False, many=True)

    class Meta:
        model = CategoryModel
        fields = (
            'id',
            'name',
            'description',
            'products',
        )


class CategoryCreateSerializer(ModelSerializer):
    # outlet = OutletListSerializer(required=False, many=True)
    class Meta:
        model = CategoryModel
        fields = (
            'name',
            # 'outlet'
        )