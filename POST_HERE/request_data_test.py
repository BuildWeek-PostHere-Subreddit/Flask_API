import unittest
from POST_HERE.request_data import jsonConversion

class MyTestCase(unittest.TestCase):
    def test_jsonConversion(self):
        self.assertEqual(jsonConversion({"title": "x", "text": "y"}), "x y")

    def test_jsonConversion_alphanumeric(self):
        self.assertEqual(jsonConversion({"title": "Hello World1", "text": "Goodbye World"}), "Hello World1 Goodbye World")

    def test_jsonConversion_notEqual(self):
        self.assertNotEqual(jsonConversion({"title": "Hello World1", "text": "Goodbye World"}), "Hello World Goodbye World111323")


if __name__ == '__main__':
    unittest.main()
