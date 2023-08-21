# Python imports
from datetime import datetime

# Django imports
from django.db import models

# Models imports
from . import Product


class PriceProduct(models.Model):
    """
    Represents the pricing information for a product over time.
    """

    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sold = models.IntegerField(default=0)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        """
        Returns a string representation of the PriceProduct.
        """
        return f'{self.id} | product: {self.product} | price: {self.price} | discount: {self.discount}'
