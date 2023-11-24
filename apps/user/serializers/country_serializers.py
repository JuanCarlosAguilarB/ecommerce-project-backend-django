# Python
# import json

# Django

# Django rest
from rest_framework import serializers

# Apps
from apps.user.models import CountryMultilanguage


class CountryMultilanguageSerializer(serializers.ModelSerializer):
    """
        Serializer for list all countries
    """

    id = serializers.IntegerField(source='country.id')
    alpha_2_code = serializers.CharField(source='country.alpha_2_code')
    abbreviation_name = serializers.CharField(
        source='country.abbreviation_name')
    dial_code = serializers.CharField(source='country.dial_code')

    class Meta:
        model = CountryMultilanguage
        fields = '__all__'
