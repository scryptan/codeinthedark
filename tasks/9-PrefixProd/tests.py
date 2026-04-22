import unittest
from solution import solve


class PrefixProductTests(unittest.TestCase):
    # Public tests
    def test_empty_array(self):
        self.assertEqual(solve([]), [])
    
    def test_single_zero(self):
        self.assertEqual(solve([0]), [0])
    
    def test_two_elements(self):
        self.assertEqual(solve([5, 3]), [5, 15])
    
    def test_three_elements(self):
        self.assertEqual(solve([4, 3, 7]), [4, 12, 84])
    
    def test_with_negative_numbers(self):
        self.assertEqual(solve([-1, -2, 2]), [-1, 2, 4])
    
    # Private tests
    def test_two_elements_large(self):
        self.assertEqual(solve([15, 30]), [15, 450])
    
    def test_with_zero_at_end(self):
        self.assertEqual(solve([4, 3, 7, 0]), [4, 12, 84, 0])


if __name__ == "__main__":
    unittest.main()