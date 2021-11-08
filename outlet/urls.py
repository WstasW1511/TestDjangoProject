from rest_framework.routers import DefaultRouter
from django.urls import re_path
from outlet.views import OutletViewSet, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('', OutletViewSet)
router.register('/category', CategoryViewSet)
router.register('/product', ProductViewSet)

urlpatterns = [
    re_path(r'^(P<pk>[0-9])/$', CategoryViewSet.as_view({'put':'update'})),
    re_path(
        r'^(?P<pk>[0-9]+)/categories/(?P<category_id>[0-9]+)/(?P<good_id>[0-9]+)/$',
        OutletViewSet.as_view({'get': 'retrieve'})
    ),
    re_path(
        r'^(?P<pk>[0-9]+)/categories/(?P<category_id>[0-9]+)/$',
        OutletViewSet.as_view({'get': 'retrieve'})
    ),
    re_path(
        r'^(?P<pk>[0-9]+)/$',
        OutletViewSet.as_view({'get': 'retrieve'})
    )
] + router.urls
