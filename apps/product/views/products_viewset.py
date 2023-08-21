# Django rest imports
from rest_framework import viewsets
from rest_framework import permissions

# Models imports
from apps.product.models import Product

# Serializers imports
from apps.product.serializers import ProductSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
