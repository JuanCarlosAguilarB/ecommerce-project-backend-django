# Django
# from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# apps
from apps.user.serializers import CreateUserSerializer

# third imports
from core.redis_config import RedisSingleton
from apps.user.task import send_verification_email, send_verification_email_sync
from apps.commons import generate_verification_code


class CreateUser(CreateAPIView):
    """Api view for create an acount for one user"""

    serializer_class = CreateUserSerializer
    permission_classes = [AllowAny]

    redis_instance = RedisSingleton().get_instance()

    def create(self, request, *args, **kwargs):
        """
        Create one user.
        """
        # in the serializers, we lets go to validate passwor2,
        # for it we lets go to pass the context at serializxers
        serializer = CreateUserSerializer(
            data=request.data, context=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user_email = user.email

        # Generate code verification
        verification_code = generate_verification_code()

        # Storing the code in Redis with a key equal to the user's email,
        # with a 15-minute expiration.
        redix_time_exp = 15 * 60  # 15 minutes or 900 seconds
        self.redis_instance.setex(
            user_email, redix_time_exp, verification_code)

        # Calling the Celery task to send the email.
        send_verification_email.delay(user_email, verification_code)
        send_verification_email_sync(user_email, verification_code)

        # we should delete password for security
        user_info = serializer.data
        user_info.pop("password")
        return Response(user_info, status=status.HTTP_201_CREATED)
