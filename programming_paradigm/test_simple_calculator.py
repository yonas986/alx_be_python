import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, -6), -10)
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6, places=7)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(0, 99), 0)
        self.assertAlmostEqual(self.calc.multiply(2.5, 0.4), 1.0, places=7)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertIsNone(self.calc.divide(10, 0))  # division by zero
        self.assertIsNone(self.calc.divide(0, 0))   # edge case


if __name__ == "__main__":
    unittest.main()
