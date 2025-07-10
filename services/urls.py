from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet, ServiceProviderViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'service-providers', ServiceProviderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
