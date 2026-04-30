import unittest
from solution import solve


class TwoSumTests(unittest.TestCase):
    # Public tests
    def test_basic_case(self):
        self.assertEqual(solve([2, 7, 11, 15], 9), [0, 1])
    
    def test_another_case(self):
        self.assertEqual(solve([3, 2, 4], 6), [1, 2])
    
    def test_with_zero(self):
        self.assertEqual(solve([0, 4, 3, 0], 0), [0, 3])
    
    def test_negative_numbers(self):
        self.assertEqual(solve([-1, -2, -3, -4, -5], -8), [2, 4])
    
    def test_minimal(self):
        self.assertEqual(solve([1, 2], 3), [0, 1])

    # Private tests
    def test_duplicates(self):
        self.assertEqual(solve([3, 3], 6), [0, 1])
    
    def test_large_numbers(self):
        self.assertEqual(solve([1000000, 500000, 500000], 1000000), [1, 2])
    
    def test_solution_at_end(self):
        self.assertEqual(solve([1, 2, 3, 4, 5, 6], 11), [4, 5])
    
    def test_solution_at_start(self):
        self.assertEqual(solve([5, 5, 1, 2], 10), [0, 1])
    
    def test_mixed_order(self):
        self.assertEqual(solve([10, -2, 3, 7], 5), [1, 3])


if __name__ == "__main__":
    unittest.main()