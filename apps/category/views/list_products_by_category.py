# Django rest imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

# Models imports
from apps.product.models import Product

# Serializers imports
from apps.product.serializers import ProductSerializer

# Commons imports
from apps.commons import PaginationHandlerMixin


class ListProductsByCategoryView(APIView, PaginationHandlerMixin):
    """
    API view to list products based on a specific category.
    Extends APIView and utilizes PaginationHandlerMixin for pagination.
    """

    # Allowing any user to access this view
    permission_classes = (permissions.AllowAny,)

    # Using the ProductSerializer to serialize the data
    serializer_class = ProductSerializer

    def get(self, request, category_id, format=None):
        """
        Handles the GET request to retrieve products of a specified category.
        """

        # Query the products for the given category ID
        queryset = Product.objects.filter(category_id=category_id)

        # If no products are found for the category, return a 404 error response
        if not queryset.exists():
            return Response({'error': 'No category products found'},
                            status=status.HTTP_404_NOT_FOUND)

        # Retrieve paginated data using the PaginationHandlerMixin
        return self.get_data_paginated(queryset=queryset,
                                       serializer_class=self.serializer_class,
                                       request=request)
