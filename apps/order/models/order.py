# Django imports
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Models imports
User = get_user_model()


class Order(models.Model):
    """
    Represents an order made by a user.
    """

    # Choices for different order statuses
    class OrderStatus(models.TextChoices):
        not_processed = 'not_processed'
        processed = 'processed'
        shipping = 'shipped'
        delivered = 'delivered'
        cancelled = 'cancelled'

    status = models.CharField(
        max_length=50, choices=OrderStatus.choices,
        default=OrderStatus.not_processed)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    full_name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state_province_region = models.CharField(max_length=255)
    postal_zip_code = models.CharField(max_length=20)
    telephone_number = models.CharField(max_length=255)
    shipping_name = models.CharField(max_length=255)
    shipping_time = models.CharField(max_length=255)
    shipping_price = models.DecimalField(max_digits=5, decimal_places=2)
    date_issued = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """
        Returns a string representation of the order.
        """
        return f'{self.id} | order id {self.transaction_id}'
