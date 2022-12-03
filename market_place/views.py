from django.shortcuts import render
from rest_framework import viewsets

from market_place import models, serializers


class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
