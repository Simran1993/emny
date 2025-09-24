from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import YourViewSet

router = DefaultRouter()
# router.register(r'endpoint', YourViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
