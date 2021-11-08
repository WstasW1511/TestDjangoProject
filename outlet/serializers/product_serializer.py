from rest_framework.serializers import ModelSerializer
from outlet.models import *


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = (
            'id',
            'title',
            'description',
            'category'
        )


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = (
            'id',
            'title',
            'description',
            'category'
        )


class ProductUpdateSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = (
            'id',
            'title',
            'description',
            'category',
            'updated'
        )

    def validate(self, attrs):
        if 'updated' in attrs:
            attrs['updated'] += 1
        return attrs
