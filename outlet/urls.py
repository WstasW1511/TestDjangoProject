from rest_framework.routers import DefaultRouter
from rest_framework.urls import path
from outlet.views import OutletViewSet, CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register('', OutletViewSet)
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)

urlpatterns = [

] + router.urls

