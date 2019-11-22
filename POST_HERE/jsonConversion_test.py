"""unittest for the jsonConversion function"""

import unittest
from functions import jsonConversion


class MyTestCase(unittest.TestCase):
    def test_jsonConversion(self):
        self.assertEqual(jsonConversion({"title": "x",
                                         "text": "y",
                                         "link": False}),
                         ["x y"])

    def test_jsonConversion_alphanumeric(self):
        self.assertEqual(jsonConversion({"title": "Hello World1",
                                         "text": "www.helloworld.com",
                                         "link": True}),
                         ["Hello World1"])

    def test_jsonConversion_notEqual(self):
        self.assertNotEqual(jsonConversion({"title": "Hello World1",
                                            "text": "Goodbye World",
                                            "link": False}),
                            ["Hello World Goodbye World111323"])


if __name__ == '__main__':
    unittest.main()
