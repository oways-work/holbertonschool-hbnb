import unittest
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity

class TestModels(unittest.TestCase):
    
    def test_user_creation(self):
        user = User("John", "Doe", "john@example.com", "123")
        self.assertEqual(user.first_name, "John")

    def test_user_invalid_email(self):
        with self.assertRaises(ValueError):
            User("John", "Doe", "not-an-email", "123")

    def test_place_creation(self):
        place = Place("Home", "Desc", 100.0, 45.0, 90.0, "user_id")
        self.assertEqual(place.price, 100.0)

    def test_place_invalid_price(self):
        with self.assertRaises(ValueError):
            Place("Home", "Desc", -10.0, 45.0, 90.0, "user_id")

    def test_amenity_creation(self):
        amenity = Amenity("WiFi")
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_empty_name(self):
        with self.assertRaises(ValueError):
            Amenity("")

if __name__ == '__main__':
    unittest.main()
