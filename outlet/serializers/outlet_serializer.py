from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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


class OutletRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutletModel
        fields = (
            'id',
        )

    def to_representation(self, instance):
        output = {}
        kwargs = self.context['kwargs']
        try:
            shop_id = kwargs['pk']
        except:
            shop_id = False
        try:
            category_id = kwargs['category_id']
        except:
            category_id = False
        try:
            good_id = kwargs['good_id']
        except:
            good_id = False
        if good_id:
            good = ProductModel.objects.filter(pk=good_id).first()
            if good:
                output = ProductListSerializer(good).data
            else:
                raise ValidationError('product id is wrong, product not found')
        elif category_id:
            category = CategoryModel.objects.filter(pk=category_id).first()
            output = CategoryListSerializer(category).data
        elif shop_id:
            shop = OutletModel.objects.filter(pk=shop_id).first()
            output = OutletSerializer(shop).data
        else:
            output = {
                'detail': 'not found any id of shop or category or product'
            }
        return output
