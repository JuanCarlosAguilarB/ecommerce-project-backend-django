# Django
from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# import ApiView
from rest_framework.views import APIView

# apps
from apps.user.serializers import VerifyAccountSerializer

# models import
from apps.user.models import User

# third imports
from core.redis_config import RedisSingleton


class VerityAccountView(APIView):
    """Api view for verify an acount of user"""

    permission_classes = [AllowAny]

    redis_instance = RedisSingleton().get_instance()

    def post(self, request, *args, **kwargs):
        """
        Validate account of user.
        """

        serializer = VerifyAccountSerializer(
            data=request.data, context=request.data)
        serializer.is_valid(raise_exception=True)

        user_email = serializer.data['email']

        # validate code of user
        code = serializer.data['code']
        code_redis = self.redis_instance.get(user_email)

        if code_redis is None:
            return Response(
                {
                    'response': {'detail': 'code not found'},
                    'error': False
                }, status=status.HTTP_404_NOT_FOUND)

        if code_redis.decode('utf-8') != code:
            return Response(
                {
                    'response': {'detail': 'code is incorrect'},
                    'error': False
                },
                status=status.HTTP_400_BAD_REQUEST)

        # delete code of redis
        self.redis_instance.delete(user_email)

        user = get_object_or_404(User, email=user_email)
        user.is_verify = True
        user.save()

        return Response({
            'response': 'ok',
            'error': False
        }, status=status.HTTP_201_CREATED)
