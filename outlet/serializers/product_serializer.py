from rest_framework.serializers import ModelSerializer
from outlet.models import *


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = (
            'id',
            'title',
            'description',

        )