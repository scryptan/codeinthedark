import unittest
from solution import solve


class MissingNumberTests(unittest.TestCase):
    # Public tests
    def test_missing_2_between_1_and_3(self):
        self.assertEqual(solve([1, 3, 4, 5]), 2)
    
    def test_missing_4_between_3_and_5(self):
        self.assertEqual(solve([1, 2, 3, 5]), 4)
    
    def test_no_missing_with_gap_at_end(self):
        self.assertEqual(solve([2, 3, 4, 5]), -1)
    
    def test_no_missing_sequential(self):
        self.assertEqual(solve([1, 2, 3, 4]), -1)
    
    def test_empty_array(self):
        self.assertEqual(solve([]), -1)
    
    # Private tests
    def test_missing_between_two_numbers(self):
        self.assertEqual(solve([333, 335]), 334)


if __name__ == "__main__":
    unittest.main()