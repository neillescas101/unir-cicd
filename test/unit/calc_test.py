import unittest
from calc import Calculator
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)
        self.assertEqual(Calculator.add(-1, 1), 0)
        with self.assertRaises(TypeError):
            Calculator.add('a', 2)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(5, 3), 2)
        with self.assertRaises(TypeError):
            Calculator.subtract(1, 'b')

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(4, 3), 12)
        with self.assertRaises(TypeError):
            Calculator.multiply(4, None)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        with self.assertRaises(TypeError):
            Calculator.divide(10, 0)
        with self.assertRaises(TypeError):
            Calculator.divide('10', 2)

    def test_power(self):
        self.assertAlmostEqual(Calculator.power(2, 3), 8)
        with self.assertRaises(TypeError):
            Calculator.power(2, 'x')

    def test_sqrt(self):
        self.assertEqual(Calculator.sqrt(9), 3)
        with self.assertRaises(TypeError):
            Calculator.sqrt(-1)
        with self.assertRaises(TypeError):
            Calculator.sqrt('a')

    def test_log10(self):
        self.assertEqual(Calculator.log10(100), 2)
        with self.assertRaises(TypeError):
            Calculator.log10(0)
        with self.assertRaises(TypeError):
            Calculator.log10(-10)
        with self.assertRaises(TypeError):
            Calculator.log10('a')

if __name__ == '__main__':
    unittest.main()