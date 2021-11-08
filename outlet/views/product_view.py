from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from outlet.models import ProductModel
from outlet.serializers import ProductListSerializer, ProductCreateSerializer, ProductUpdateSerializer


class ProductViewSet(ListModelMixin,
                     CreateModelMixin,
                     UpdateModelMixin,
                     GenericViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductListSerializer

    def get_serializer_class(self):
        serializer_class = ProductListSerializer
        if self.action == 'create':
            serializer_class = ProductCreateSerializer
        if self.action == 'list':
            serializer_class = ProductListSerializer
        elif self.action == 'update':
            serializer_class = ProductUpdateSerializer
        return serializer_class


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = ProductListSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
