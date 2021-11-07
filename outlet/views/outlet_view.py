from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet



from outlet.models import OutletModel
from outlet.serializers import OutletListSerializer, OutletCreateSerializer,OutletSerializer


class OutletViewSet(ListModelMixin,
                    CreateModelMixin,
                    GenericViewSet):
    queryset = OutletModel.objects.all()
    serializer_class = OutletSerializer

    def get_serializer_class(self):
        serializer_class = OutletListSerializer
        if self.action == 'create':
            serializer_class = OutletCreateSerializer
        elif self.action == 'list':
            serializer_class = OutletSerializer
        # elif self.action == 'update':
        #     serializer_class = PostUpdateSerializer
        return serializer_class


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        serializer_data = OutletListSerializer(instance).data
        return Response(data=serializer_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
