# Python
# import json

# Django


# Django rest
from rest_framework import serializers

# Apps
from apps.user.models import User


class DeleteAccount(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password',)

    def validate_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})
        return value
