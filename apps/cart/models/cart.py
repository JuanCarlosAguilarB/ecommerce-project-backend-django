# Django imports
from django.db import models
from django.conf import settings

# models imports
User = settings.AUTH_USER_MODEL


class Cart(models.Model):
    """
    Represents the cart of shop of user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_items = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id} | total items: {self.total_items}'
