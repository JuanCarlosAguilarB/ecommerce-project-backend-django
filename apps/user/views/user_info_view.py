# Django
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Django Rest Framework
from rest_framework import status, viewsets
from rest_framework.response import Response

# apps
from apps.user.serializers import CreateUserSerializer, ListUserSerializer
from apps.user.models import User
from apps.commons import ListModelMixin


class UserViewSet(viewsets.ViewSet):
    """
    get info of user
    """
    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = ListUserSerializer(user)
        return Response(serializer.data)

    # permission_classes = [IsAdminUser]
