# Django rest imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
# from rest_framework.permissions import IsAdminUser

# Models imports
from apps.category.models import Category

# Serializers imports


class ListCategoriesView(APIView):
    """
    API view to list categories and their sub-categories.
    """

    # Allowing any user to access this view
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        """
        Handles the GET request to retrieve categories and their sub-categories.
        """

        # Check if any categories exist in the database
        if Category.objects.all().exists():

            # Query all categories
            categories = Category.objects.all()

            result = []

            for category in categories:
                # Check if the category has no parent (top-level category)
                if not category.parent:
                    item = {}
                    item['id'] = category.id
                    item['name'] = category.name

                    item['sub_categories'] = []

                    for cat in categories:
                        sub_item = {}

                        # Check if the current category is a sub-category of the current top-level category
                        if cat.parent and cat.parent.id == category.id:
                            sub_item['id'] = cat.id
                            sub_item['name'] = cat.name
                            sub_item['sub_categories'] = []

                            item['sub_categories'].append(sub_item)

                    result.append(item)

            return Response({'categories': result}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No categories found'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
