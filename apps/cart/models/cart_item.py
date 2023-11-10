# Django imports
from django.db import models
from apps.product.models import Product

# models imports
from apps.cart.models import Cart


class CartItemManager(models.Manager):

    def create(self, cart, product, count):

        # don't create a new cart item if there is already one
        existing_cart_item = self.filter(cart=cart, product=product).first()

        if existing_cart_item:
            # if exits a cart item, update the count
            cart.total_items += count
            cart.save()

            existing_cart_item.count += count
            existing_cart_item.save()
            return existing_cart_item

        # if dont exits a cart item, create a new one
        cart_item = self.model(cart=cart, product=product, count=count)
        cart_item.save()
        return cart_item


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    objects = CartItemManager()

    # if a item is saved, the total_items of the cart will be updated

    def save(self, *args, **kwargs):
        self.cart.total_items += self.count
        self.cart.save()
        super().save(*args, **kwargs)

    # if a item is deleted, the total_items of the cart will be updated

    def delete(self, *args, **kwargs):
        self.cart.total_items -= self.count
        self.cart.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.id} | product name: {self.product.name}'
