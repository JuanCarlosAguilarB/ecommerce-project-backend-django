# python imports
from datetime import datetime

# Django imports
from django.db import models

# Models imports
from apps.category.models import Category


class Product(models.Model):
    """
    Represents a product in the application's inventory.
    """

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=datetime.now)

    def get_thumbnail(self):
        """
        Returns the URL of the product's thumbnail photo.
        If no photo is available, returns an empty string.
        """
        if self.photo:
            return self.photo.url
        return ''

    def __str__(self):
        """
        Returns a string representation of the product (its name).
        """
        return f'{self.id} | {self.name}'