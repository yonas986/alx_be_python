import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    # --- add ---
    def test_addition_integers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, -6), -10)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_addition_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6, places=7)
        self.assertAlmostEqual(self.calc.add(-2.5, 2.5), 0.0, places=7)

    def test_addition_commutative(self):
        a, b = 7, 11
        self.assertEqual(self.calc.add(a, b), self.calc.add(b, a))

    # --- subtract ---
    def test_subtraction_integers(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtraction_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3, places=7)

    def test_subtraction_non_commutative(self):
        self.assertNotEqual(self.calc.subtract(9, 4), self.calc.subtract(4, 9))

    # --- multiply ---
    def test_multiplication_integers(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(0, 99), 0)

    def test_multiplication_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 0.4), 1.0, places=7)

    def test_multiplication_commutative(self):
        a, b = 8, 5
        self.assertEqual(self.calc.multiply(a, b), self.calc.multiply(b, a))

    # --- divide ---
    def test_division_normal(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)
        self.assertEqual(self.calc.divide(-9, 3), -3)

    def test_division_by_zero_returns_none(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_non_commutative(self):
        self.assertNotEqual(self.calc.divide(8, 2), self.calc.divide(2, 8))


if __name__ == "__main__":
    unittest.main()
