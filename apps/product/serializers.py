# Django imports
from django.utils import timezone
from django.db.models import Q

# Django rest imports
from rest_framework import serializers

# models imports
from .models import Product, PriceProduct


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializes the Product model for API representation.
    Provides additional calculated fields related to pricing.
    """

    # Additional fields to be included in the serialized data
    normal_price = serializers.SerializerMethodField()
    calculated_price = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'  # Include all fields from the Product model

    def get_prices(self, obj):
        """
        Returns the PriceProduct object associated with the current time and the given product.
        """
        now = timezone.now()

        return PriceProduct.objects.filter(
            Q(end_date__isnull=True) | Q(end_date__gte=now),
            product=obj,
            start_date__lte=now,
            # end_date__gte=now
        ).first()

    def get_normal_price(self, obj):
        """
        Returns the normal price of the product based on the associated PriceProduct object.
        If no PriceProduct is found, returns 0.
        """
        price_product = self.get_prices(obj)
        if not price_product:
            return 0
        return price_product.price

    def get_calculated_price(self, obj):
        """
        Returns the calculated price of the product by subtracting the discount from the PriceProduct price.
        If no PriceProduct is found, returns 0.
        """
        price_product = self.get_prices(obj)
        if not price_product:
            return 0
        return price_product.price - price_product.discount

    def get_discount(self, obj):
        """
        Returns the discount amount for the product based on the associated PriceProduct object.
        If no PriceProduct is found, returns 0.
        """
        price_product = self.get_prices(obj)
        if not price_product:
            return 0
        return price_product.discount
