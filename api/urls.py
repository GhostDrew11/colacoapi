from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('sodas', views.SodaViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]