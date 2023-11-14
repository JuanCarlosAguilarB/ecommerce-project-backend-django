# Django
from django.shortcuts import get_object_or_404
from django.http import Http404

# Django Rest Framework
from rest_framework import status, viewsets
from rest_framework.response import Response

# apps
from apps.user.serializers import CreateUserSerializer, ListUserSerializer
from apps.user.models import User
from apps.commons import ListModelMixin


# class UserViewSet(ListModelMixin, viewsets.GenericViewSet, viewsets.ViewSet):
#     """
#     List of users with active acounts .
#     """
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         # los usuarios con status son los usuarios con cuentas activas
#         return queryset.filter(status=True)

#     # permission_classes = [IsAdminUser]

# get info of user
class UserViewSet(viewsets.ViewSet):
    """
    get info of user
    """

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = ListUserSerializer(user)
        return Response(serializer.data)

    # permission_classes = [IsAdminUser]