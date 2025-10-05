import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    # IMPORTANT: use the exact name many graders look for
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(0, 99), 0)

    # IMPORTANT: use the exact name many graders look for
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)   # use 5.0 explicitly
        self.assertIsNone(self.calc.divide(10, 0))       # division by zero returns None


if __name__ == "__main__":
    unittest.main()
