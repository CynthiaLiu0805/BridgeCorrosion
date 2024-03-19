import unittest
import inputCheck

class TestInputCheck(unittest.TestCase):
    def test_point_in_boundary(self):
        latitude = 40.7128
        longitude = -74.0060
        result = inputCheck.is_within_ontario(latitude, longitude)
        self.assertTrue(result)

    def test_point_not_in_boundary(self):
        latitude = 48.4284
        longitude = -123.3656
        result = inputCheck.is_within_ontario(latitude, longitude)
        self.assertFalse(result)
    
    def test_value_error(self):
        latitude = "abc"
        longitude = -123.3656
        with self.assertRaises(ValueError):
            inputCheck.is_within_ontario(latitude, longitude)
            
    def test_value_error_empty(self):
        latitude = ""
        longitude = -123.3656
        with self.assertRaises(ValueError):
            inputCheck.is_within_ontario(latitude, longitude)
    
if __name__ == '__main__':
    unittest.main()