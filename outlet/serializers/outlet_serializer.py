from rest_framework import serializers
from outlet.models import *
from .category_serializer import CategoryListSerializer,CategoryCreateSerializer
from .product_serializer import ProductListSerializer

class OutletListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(required=False)
    product = ProductListSerializer(required=False)
    class Meta:
        model = OutletModel
        fields = (
            'id',
            'name',
            'category',
            'product'
        )

class OutletCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutletModel
        fields = (
            'id',
            'name',
            # 'category'

        )


class OutletSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(required=False, many=True)

    class Meta:
        model = OutletModel
        fields = (
            'id',
            'name',
            'categories',
        )
