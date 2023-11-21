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
    date_created = models.DateTimeField(default=datetime.now)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # prevent modify price after create
    def save(self, *args, **kwargs):
        if self.pk is not None:
            raise ValueError("PriceProduct can't be modified after create")

        # set active to false for all other PriceProduct of the same product
        PriceProduct.objects.filter(product=self.product).update(active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the PriceProduct.
        """
        return f'{self.id} | product: {self.product} | price: {self.price}'
