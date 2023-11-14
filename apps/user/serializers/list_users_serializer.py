# Python
# import json


# Django rest
from rest_framework import serializers

# Apps
from apps.user.models import User


class ListUserSerializer(serializers.ModelSerializer):
    """
    serializers for list all users
    """
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('password', 'user_permissions', 'is_superuser',
                   'last_login', 'is_staff', 'is_active', 'groups', 'status')

    def get_full_name(self, obj):
        first_name = obj.first_name or ''
        last_name = obj.last_name or ''
        return f'{first_name} {last_name}'
