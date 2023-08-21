# Django imports
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Models imports
from .order import Order
from apps.product.models import Product

User = get_user_model()


class OrderItem(models.Model):
    """
    Represents an item within an order.
    """

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """
        Returns a string representation of the order item (its name).
        """
        return self.name
