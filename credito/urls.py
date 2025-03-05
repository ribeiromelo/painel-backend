from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreditoClienteViewSet

router = DefaultRouter()
router.register(r'credito', CreditoClienteViewSet, basename='credito')

urlpatterns = [
    path('', include(router.urls)),
]
