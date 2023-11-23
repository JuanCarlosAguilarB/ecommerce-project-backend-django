# Django imports for testing
from django.test import TestCase

# Models imports for testing
from apps.category.models import Category
from apps.product.models import Product
from apps.product.models.auditory_product_amount import AuditoryProductAmount


class ProductTestCase(TestCase):
    """
    Test cases for the Product model functionalities.
    """

    def setUp(self):
        """
        Prepare test data: creates a category and a product.
        """
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            category=self.category,
            quantity=10
        )

    def test_auditory_product_amount_creation(self):
        """
        Verify if AuditoryProductAmount is created when a product is created.
        """
        auditory_product_amount = AuditoryProductAmount.objects.get(
            product=self.product)
        self.assertEqual(auditory_product_amount.amount, self.product.quantity)

    def test_auditories_product_amount_creation(self):
        """
        Verify if several AuditoryProductAmount are
        created when an amount of product is updated.
        """
        old_quantity = self.product.quantity
        self.product.quantity = 15
        self.product.save()

        auditory_product_amount = AuditoryProductAmount.objects.filter(
            product=self.product).order_by('-date_created')

        self.assertEqual(
            auditory_product_amount.count(), 2)

        self.assertEqual(
            auditory_product_amount[0].amount, self.product.quantity)

        self.assertEqual(
            auditory_product_amount[1].amount, old_quantity)

    def test_delete_prevention(self):
        """
        Verify that the product deletion raises a ValueError.
        """
        with self.assertRaises(ValueError):
            self.product.delete()
