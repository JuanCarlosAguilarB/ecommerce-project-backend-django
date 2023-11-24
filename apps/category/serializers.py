# Django rest imports
from rest_framework import serializers

# models imports
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializes the Category model for API representation.
    """

    class Meta:
        model = Category
        fields = '__all__'
