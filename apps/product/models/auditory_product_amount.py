# python imports
from datetime import datetime
import uuid

# Django imports
from django.db import models

# Models imports
# from apps.product.models.product import Product


class AuditoryProductAmount(models.Model):
    """
    save the amount of a product in a specific date for auditory purposes.
    """
    product = models.ForeignKey(
        'Product',
        on_delete=models.PROTECT,
        blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.now)
    amount = models.IntegerField()

    # prevent to delete a UserPurchase
    def delete(self, *args, **kwargs):
        raise ValueError("User purchase can't deleted")

    def __str__(self):
        """
        Returns a string representation.
        """
        return f'{self.id} - amount: {self.amount}'
