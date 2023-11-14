# Django
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator

# Django Rest Framework
from rest_framework import status, viewsets
# from rest_framework.response import Response

# apps
from apps.user.serializers import CreateUserSerializer  # , ListUserSerializer
from apps.user.models import User
from apps.commons import ListModelMixin


# django redis
from django.views.decorators.cache import cache_page


@method_decorator(cache_page(60 * 15), name='dispatch')
class ListUserViewSet(ListModelMixin, viewsets.GenericViewSet,
                      viewsets.ViewSet):
    """
    List of users with active acounts .
    """
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        # los usuarios con status son los usuarios con cuentas activas
        return queryset.filter(status=True)

    # permission_classes = [IsAdminUser]
