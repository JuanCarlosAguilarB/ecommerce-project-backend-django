# Python
# import json

# Django
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

# Django rest
from rest_framework import serializers

# Apps
from apps.user.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """
    serializers for create an user with corfimn password
    """

    # field by verify password
    password2 = serializers.CharField(write_only=True)

    def validate_password2(self, value):
        """
        Funtion for validate password
        """

        if value != self.context["password"]:
            raise serializers.ValidationError(_("password don't match"))

    def create(self, validated_data):
        """
        Funtion for to create a user
        """
        validated_data.pop("password2")

        # is needly to encripted  the password
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        exclude = ('user_permissions',
                   'is_superuser',
                   'last_login',
                   'is_staff',
                   'is_active',
                   'groups',
                   'status',
                   )
