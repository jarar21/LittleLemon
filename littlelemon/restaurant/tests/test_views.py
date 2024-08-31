from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        # Add test instances of the Menu model
        self.menu1 = Menu.objects.create(name="Pasta", price=10.99, inventory=10)
        self.menu2 = Menu.objects.create(name="Pizza", price=12.99, inventory=20)
        self.menu3 = Menu.objects.create(name="Salad", price=8.99, inventory=15)

    def test_get_all(self):
        # Retrieve all Menu objects
        menus = Menu.objects.all()
        
        # Serialize the data
        serializer = MenuSerializer(menus, many=True)
        
        # Define the expected serialized data with 'id' fields
        expected_data = [
            {'id': self.menu1.id, 'name': 'Pasta', 'price': '10.99', 'inventory': 10},
            {'id': self.menu2.id, 'name': 'Pizza', 'price': '12.99', 'inventory': 20},
            {'id': self.menu3.id, 'name': 'Salad', 'price': '8.99', 'inventory': 15},
        ]
        
        # Assert that the serialized data matches the expected data
        self.assertEqual(serializer.data, expected_data)
