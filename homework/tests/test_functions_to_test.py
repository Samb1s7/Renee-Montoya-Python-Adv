import unittest
from functions_to_test import Calculator

class Test_Calculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(1,2), 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(5,2), 3)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(3,4), 12)

    def test_devide(self):
        self.assertRaises(ValueError, Calculator.divide, 4, 0)
        self.assertEqual(Calculator.divide(9,3), 3)

# pytho3 -m unittest