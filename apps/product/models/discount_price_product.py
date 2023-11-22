# Python imports
from datetime import datetime

# Django imports
from django.db import models

# Models imports
from . import PriceProduct


class DiscountPriceProduct(models.Model):
    """
    Represents the pricing information for a product over time.
    """

    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField()
    price_product = models.ForeignKey(PriceProduct, on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    @property
    def active(self):
        """
        Returns whether the PriceProduct is active or not.
        """
        return self.start_date < datetime.now() < self.end_date

    def save(self, *args, **kwargs):
        if not self.price_product.active:
            raise ValueError("PriceProduct is not active")

        # self.start_date shoul be greather datetime.now()
        if self.start_date < datetime.now():
            raise ValueError("start_date should be greather to now")

        # self.end_date shoul be greather self.start_date
        if self.end_date < self.start_date:
            raise ValueError("end_date should be greather start_date")

        # prevent to save the DiscountPriceProduct
        # if the PriceProduct is not active
        if not self.price_product.active:
            raise ValueError("PriceProduct is not active")

        # prevent a DiscountPriceProduct from being created
        # if its start_date and end_date are between other
        # start_date and end_date of another DiscountPriceProduct

        if DiscountPriceProduct.objects.filter(
                price_product=self.price_product,
                start_date__lte=self.start_date,
                end_date__gte=self.end_date
        ).exists():
            raise ValueError("Another DiscountPriceProduct is active")

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        if self.start_date < datetime.now():
            raise ValueError("User purchase can't deleted")

        super().delete(*args, **kwargs)

    def __str__(self):
        """
        Returns a string representation of the PriceProduct.
        """
        return f'{self.id} | price: {self.price_product.price} | discount: {self.discount}'
