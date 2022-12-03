from django.urls import path, include

from market_place import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product', views.ProductView)


urlpatterns = [
    path('', include(router.urls)),
]