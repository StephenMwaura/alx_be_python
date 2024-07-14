import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-2,2), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract|(9,4), 5)
    def test_multiplication(self):
        self.assertEqual(self.test_multiply(6,6),36)
    def test_division(self):
        self.assertEqual(self.calc.divide(10,5),2)
        with self.assertRaises(ZeroDivisionError):
            (self.calc.divide(5,0),0)