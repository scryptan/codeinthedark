import unittest
from solution import solve


class SumFromXToYTests(unittest.TestCase):
    # Public tests
    def test_zero_to_zero(self):
        self.assertEqual(solve(0, 0), 0)
    
    def test_one_to_ten(self):
        self.assertEqual(solve(1, 10), 55)
    
    def test_two_to_five(self):
        self.assertEqual(solve(2, 5), 14)
    
    def test_negative_to_zero(self):
        self.assertEqual(solve(-7, 0), -28)
    
    # Private tests
    def test_negative_to_positive(self):
        self.assertEqual(solve(-1, 4), 9)


if __name__ == "__main__":
    unittest.main()