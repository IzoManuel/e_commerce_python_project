from django.test import TestCase
from django.utils import timezone
from products.models import Category

class CategoryModelTest(TestCase):
    def setUp(self):

        self.category_data = {
            'name' : 'TestCategory',
            'description' : 'Test Description'
        }

        self.category = Category.objects.create(**self.category_data)

    def test_category_list(self):
        categories = Category.objects.all()

        self.assertIn(self.category, categories)

    def test_category_creation(self):
        saved_category = Category.objects.get(name = 'TestCategory')

        self.assertEqual(saved_category.name, 'TestCategory')

    def test_category_update(self):
        new_description = 'Update Test Description'
        self.category.description = new_description
        self.category.save()

        updated_category = Category.objects.get(name = 'TestCategory')

        self.assertEqual(updated_category.description, new_description)

    def test_category_delete(self):
        self.category.delete()

        with self.assertRaises(Category.DoesNotExist):
            deleted_category = Category.objects.get(name = 'TestCategory')
