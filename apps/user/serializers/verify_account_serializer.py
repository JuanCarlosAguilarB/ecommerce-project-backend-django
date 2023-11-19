# Django rest
from rest_framework import serializers


class VerifyAccountSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    code = serializers.CharField(required=True)
