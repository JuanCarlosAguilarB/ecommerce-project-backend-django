from django.shortcuts import render
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
