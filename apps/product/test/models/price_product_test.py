# django imports for testing
from django.test import TestCase

# Models imports for testing
from apps.product.models import PriceProduct, Product


class PriceProductTestCase(TestCase):
    """
    Test cases for the PriceProduct model functionalities.
    """

    def setUp(self):
        """
        Prepare test data: creates a product and a price product instance.
        """
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            quantity=10
        )
        self.price_product = PriceProduct.objects.create(
            product=self.product,
            active=True,
            price=50.00
        )

    def test_prevent_modify_price_after_create(self):
        """
        Verify that modification of PriceProduct after creation raises
        a ValueError.
        """
        # Try modifying the price after creation
        self.price_product.price = 60.00

        with self.assertRaises(ValueError):
            self.price_product.save()

    def test_set_active_false_for_other_price_products(self):
        """
        Verify if setting active to false for all other PriceProduct
        instances of the same product works.
        """
        # Create another PriceProduct instance for the same product
        another_price_product = PriceProduct.objects.create(
            product=self.product,
            # active=True,
            price=70.00
        )

        # Check that the original price product is inactive
        # after the creation of another price product
        self.price_product.refresh_from_db()
        self.assertFalse(self.price_product.active)

        # Check that the newly created price product is active
        another_price_product.refresh_from_db()
        self.assertTrue(another_price_product.active)
