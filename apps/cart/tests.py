# Django imports
from django.test import TestCase
from django.db.models import Sum

# Models imports
from apps.cart.models import Cart, CartItem
from apps.user.models import User
from apps.product.models import Product


class CartModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@example.com', password='testpassword')
        self.cart = Cart.objects.create(user=self.user, total_items=0)
        self.product = Product.objects.create(
            name='Test Product', photo='', description='Test Description',
            quantity=10)
        self.cart_item = CartItem.objects.create(
            cart=self.cart, product=self.product, count=1)

    def test_cart_total_items(self):
        """
        Test the total_items field of the cart
            should be equal to the sum of the count of all cart items.
        """

        initial_total_items = self.cart.total_items
        total_items = CartItem.objects.filter(
            cart=self.cart).aggregate(Sum('count'))
        self.assertEqual(
            total_items['count__sum'],
            initial_total_items)

    def test_cart_item_save_method(self):
        """
        Test the save method of the cart item.
        """

        cart_item = CartItem.objects.create(
            cart=self.cart, product=self.product, count=2)

        total_items = CartItem.objects.filter(
            cart=self.cart).aggregate(Sum('count'))

        self.assertEqual(total_items['count__sum'],
                         self.cart.total_items)

    def test_cart_item_delete_method(self):
        """
        Test the delate  method of the cart item.
        """

        initial_total_items = self.cart.total_items

        self.cart_item.delete()

        updated_cart = Cart.objects.get(pk=self.cart.pk)

        self.assertEqual(updated_cart.total_items,
                         initial_total_items - self.cart_item.count)

    def test_dont_create_new_cart_item_if_already_exists(self):
        """
        Test that a new cart item is not created if there is already one.
        """

        cart_item = CartItem.objects.create(
            cart=self.cart, product=self.product, count=2)

        cart_items = CartItem.objects.filter(
            cart=self.cart, product=self.product)

        amount_cart_items = cart_items.count()

        # don't create a new cart item if there is already one
        self.assertEqual(amount_cart_items, 1)
