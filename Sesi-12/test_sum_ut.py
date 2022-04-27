from fractions import Fraction
import unittest
from sum import sum_self_made

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_self_made([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum_self_made((1, 2, 3)), 6, "Should be 6")

    def test_sum_fraction(self):
        data = [Fraction(1, 4), Fraction(3, 4)]
        self.assertEqual(sum_self_made(data), 1, "Should be 1")

if __name__ == "__main__":
    unittest.main()