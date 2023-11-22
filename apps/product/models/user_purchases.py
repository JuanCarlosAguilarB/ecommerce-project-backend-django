# python imports
from datetime import datetime
import uuid

# Django imports
from django.db import models

# Models imports
from apps.user.models import User
from apps.product.models import PriceProduct, DiscountPriceProduct


class UserPurchase(models.Model):
    """
    Represents a user purchase in the application's inventory.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_purchase = models.DateTimeField(default=datetime.now)
    price_product = models.ForeignKey(
        PriceProduct,
        on_delete=models.PROTECT,
        blank=True, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True, null=True)
    amount = models.IntegerField(default=0)

    discount_price_product = models.ForeignKey(
        DiscountPriceProduct,
        on_delete=models.PROTECT,
        blank=True, null=True)

    # prevent to delete a UserPurchase
    def delete(self, *args, **kwargs):
        raise ValueError("User purchase can't deleted")

    def __str__(self):
        """
        Returns a string representation of the product (its name).
        """
        return f'{self.id}'
