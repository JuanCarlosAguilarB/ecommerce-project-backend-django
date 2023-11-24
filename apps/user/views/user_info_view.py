# Django
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Django Rest Framework
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# apps
from apps.user.serializers import CreateUserSerializer, ListUserSerializer, UpdateUserSerializer
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

# update user info


class UpdateUserProfileView(generics.UpdateAPIView):
    """
    update user info
    """
    serializer_class = UpdateUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return self.request.user
        except Http404:
            raise Http404
