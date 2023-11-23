# python imports
from datetime import datetime

# Django imports
from django.db import models

# Models imports
from apps.category.models import Category
from apps.product.models.auditory_product_amount import AuditoryProductAmount


class Product(models.Model):
    """
    Represents a product in the application's inventory.
    """

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True, null=True)
    quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.now)

    available = models.BooleanField(default=True)

    def get_thumbnail(self):
        """
        Returns the URL of the product's thumbnail photo.
        If no photo is available, returns an empty string.
        """
        if self.photo:
            return self.photo.url
        return ''

    # prevent to delete a UserPurchase
    def delete(self, *args, **kwargs):
        raise ValueError("Product can't be to delete")

    # save in AuditoryProductAmount the amount of the product
    # when the product is created or updated
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        AuditoryProductAmount.objects.create(
            product=self,
            amount=self.quantity
        )

    def __str__(self):
        """
        Returns a string representation of the product (its name).
        """
        return f'{self.id} | {self.name}'
