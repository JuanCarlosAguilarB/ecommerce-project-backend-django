# Django
from django.http import Http404

# Django Rest Framework
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

# apps
from apps.user.serializers import DeleteAccount
from apps.user.models import User


class DeleteUserAcount(RetrieveAPIView):
    """Delete account of one user"""

    serializer_class = DeleteAccount
    # for to search by username, see the next
    # https://github.com/encode/django-rest-framework/issues/6005
    lookup_field = 'username'
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        # extraer el username del url
        username = self.kwargs['username']
        user = User.objects.filter(username=username)
        if not user:
            raise Http404("No MyModel matches the given query.")

        return user

    def retrieve(self, request, username, pk=None):
        instance = self.get_object()
        # query = request.GET.get('query', None)  # read extra data
        instance.status = False
        instance.save()
        return Response(self.serializer_class(instance).data,
                        status=status.HTTP_200_OK)
