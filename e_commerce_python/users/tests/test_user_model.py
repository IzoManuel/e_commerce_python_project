from django.test import TestCase
from django.utils import timezone
from users.models import User

class CategoryModelTest(TestCase):
    def setUp(self):

        self.category_data = {
            'name' : 'TestCategory',
            'description' : 'Test Description'
        }

        self.user = User.objects.create(**self.category_data)

    def test_category_list(self):
        users = User.objects.all()

        self.assertIn(self.user, users)

    def test_category_creation(self):
        saved_category = User.objects.get(name = 'TestCategory')

        self.assertEqual(saved_category.name, 'TestCategory')

    def test_category_update(self):
        new_description = 'Update Test Description'
        self.user.description = new_description
        self.user.save()

        updated_category = User.objects.get(name = 'TestCategory')

        self.assertEqual(updated_category.description, new_description)

    def test_category_delete(self):
        self.user.delete()

        with self.assertRaises(User.DoesNotExist):
            deleted_category = User.objects.get(name = 'TestCategory')
