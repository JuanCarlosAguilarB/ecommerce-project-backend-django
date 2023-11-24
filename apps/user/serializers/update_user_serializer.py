# Python
# import json

# Django
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

# Django rest
from rest_framework import serializers

# Apps
from apps.user.models import User


class UpdateUserSerializer(serializers.ModelSerializer):
    """
    serializers for update the user information
    """

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'phone',
                  'country',
                  'email',
                  'username',
                  'photo',
                  'address',
                  'city',
                  )
