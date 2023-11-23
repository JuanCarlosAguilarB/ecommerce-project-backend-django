# python imports
from datetime import datetime, timedelta

# django imports for testing
from django.test import TestCase

# models imports for testing
from apps.product.models import DiscountPriceProduct, PriceProduct, Product


class DiscountPriceProductTestCase(TestCase):
    """
    Test cases for the DiscountPriceProduct model functionalities.
    """

    def setUp(self):
        """
        Prepare test data: creates a PriceProduct and a DiscountPriceProduct
        instance.
        """

        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            quantity=10
        )
        self.price_product = PriceProduct.objects.create(
            product=self.product,
            active=True,
            price=100.00
        )
        self.discount_price_product = DiscountPriceProduct.objects.create(
            start_date=datetime.now() + timedelta(days=1),
            end_date=datetime.now() + timedelta(days=2),
            price_product=self.price_product,
            discount=20.00
        )

    def test_discount_price_product_creation(self):
        """
        Verify if a DiscountPriceProduct instance is created correctly.
        """
        self.assertIsInstance(self.discount_price_product,
                              DiscountPriceProduct)
        self.assertEqual(
            self.discount_price_product.price_product, self.price_product)
        self.assertEqual(self.discount_price_product.discount, 20.00)
        self.assertFalse(self.discount_price_product.active)

    # def test_start_date_greater_than_now(self):
    #     """
    #     Verify that start_date should be greater than datetime.now().
    #     """
    #     with self.assertRaises(ValueError):
    #         DiscountPriceProduct.objects.create(
    #             start_date=datetime.now() - timedelta(days=2),
    #             end_date=datetime.now() + timedelta(days=1),
    #             price_product=self.price_product,
    #             discount=10.00
    #         )

    # def test_end_date_greater_than_start_date(self):
    #     """
    #     Verify that end_date should be greater than start_date.
    #     """
    #     with self.assertRaises(ValueError):
    #         DiscountPriceProduct.objects.create(
    #             start_date=datetime.now(),
    #             end_date=datetime.now() - timedelta(days=1),
    #             price_product=self.price_product,
    #             discount=10.00
    #         )

    # def test_price_product_active_check(self):
    #     """
    #     Verify that a DiscountPriceProduct can only be saved if the associated PriceProduct is active.
    #     """
    #     inactive_price_product = PriceProduct.objects.create(
    #         product_id=2,
    #         active=False,
    #         price=200.00
    #     )
    #     with self.assertRaises(ValueError):
    #         DiscountPriceProduct.objects.create(
    #             start_date=datetime.now(),
    #             end_date=datetime.now() + timedelta(days=1),
    #             price_product=inactive_price_product,
    #             discount=15.00
    #         )

    # def test_overlapping_discounts(self):
    #     """
    #     Verify that a DiscountPriceProduct cannot overlap with another DiscountPriceProduct.
    #     """
    #     # Create another DiscountPriceProduct with overlapping dates
    #     overlapping_discount = DiscountPriceProduct.objects.create(
    #         start_date=datetime.now() - timedelta(days=1),
    #         end_date=datetime.now() + timedelta(days=2),
    #         price_product=self.price_product,
    #         discount=30.00
    #     )

    #     # Verify that the creation of overlapping discounts raises a ValueError
    #     with self.assertRaises(ValueError):
    #         overlapping_discount.save()

    # def test_delete_prevention(self):
    #     """
    #     Verify that deletion of DiscountPriceProduct is prevented after start_date.
    #     """
    #     with self.assertRaises(ValueError):
    #         self.discount_price_product.delete()
