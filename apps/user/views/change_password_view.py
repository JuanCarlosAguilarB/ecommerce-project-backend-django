# Django
# from django.shortcuts import get_object_or_404
from django.http import Http404

# Django Rest Framework
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

# apps
from apps.user.serializers import ChangePasswordSerializer
from apps.user.models import User


class ChangePasswordView(UpdateAPIView):
    """Change password of an user"""

    # para buscar por username, see the next
    # https://github.com/encode/django-rest-framework/issues/6005
    lookup_field = 'username'
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        # extraer el username del url
        username = self.kwargs['username']
        user = User.objects.filter(username=username)
        if not user:
            raise Http404("No MyModel matches the given query.")

        return user
    serializer_class = ChangePasswordSerializer
