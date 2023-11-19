# Django Rest Framework
from rest_framework.response import Response


class ListModelMixin:
    """
    Mixin for listing a queryset with pagination for GenericViewSet.
    """

    def list(self, request, *args, **kwargs):
        """
        Handles the listing of a queryset with pagination.
        """

        # Get the queryset based on the view's defined get_queryset method
        queryset = self.get_queryset()

        # Attempt to paginate the queryset
        page = self.paginate_queryset(queryset)

        # If pagination is applied, serialize and return paginated data
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # If no pagination is applied, serialize and return the entire queryset
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
