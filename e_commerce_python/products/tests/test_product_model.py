from django.test import TestCase
from django.utils import timezone
from users.models import User
from products.models import Product, Category
from decimal import Decimal

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='1234')

        self.category = Category.objects.create(name='TestCategory')

        self.product_data = {
            'name' : 'TestProduct',
            'added_by' : 'admin',
            'user_id' : self.user,
            'category_id' : self.category,
            'unit_price' : 19.99,
            'created_at' : timezone.now(),
        }

        self.product = Product.objects.create(**self.product_data)

    def test_product_list(self):
        products = Product.objects.all()

        self.assertIn(self.product, products)

    def test_product_creation(self):
        saved_product = Product.objects.get(name = 'TestProduct')

        self.assertEqual(saved_product.name, 'TestProduct')
        self.assertEqual(saved_product.added_by, 'admin')
        self.assertEqual(saved_product.user_id, self.user)
        self.assertEqual(saved_product.category_id, self.category)
        self.assertEqual(saved_product.unit_price, Decimal('19.99'))
        self.assertTrue(isinstance(saved_product.created_at, timezone.datetime))

    def test_product_update(self):
        new_unit_price = Decimal('29.99')
        self.product.unit_price = new_unit_price
        self.product.save()

        updated_product = Product.objects.get(name = 'TestProduct')

        self.assertEqual(updated_product.unit_price, new_unit_price)

    def test_product_delete(self):
        self.product.delete()

        with self.assertRaises(Product.DoesNotExist):
            deleted_product = Product.objects.get(name = 'TestProduct')
