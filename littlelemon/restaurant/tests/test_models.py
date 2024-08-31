from django.test import TestCase
from restaurant.models import Menu

class TestMenu(TestCase):
    def test_str(self):
        item = Menu.objects.create(name="Icecream", price=54.99, inventory=10)
        self.assertEqual(str(item), "Icecream : $54.99")