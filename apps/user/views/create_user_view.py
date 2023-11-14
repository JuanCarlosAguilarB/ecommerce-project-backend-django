# Django
# from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# apps
from apps.user.serializers import CreateUserSerializer


##
class CreateUser(CreateAPIView):
    """Api view for create an acount for one user"""

    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Create one user.
        """
        # in the serializers, we lets go to validate passwor2,
        # for it we lets go to pass the context at serializxers
        serializer = CreateUserSerializer(
            data=request.data, context=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # we should delete password for security
        user_info = serializer.data
        user_info.pop("password")
        return Response(user_info, status=status.HTTP_201_CREATED)
