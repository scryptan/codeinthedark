import unittest
from solution import solve


class MedianTests(unittest.TestCase):
    # Public tests
    def test_empty_array(self):
        self.assertEqual(solve([]), -1)
    
    def test_single_element(self):
        self.assertEqual(solve([1]), 1)
    
    def test_odd_length_three_elements(self):
        self.assertEqual(solve([1, 2, 3]), 2)
    
    def test_even_length_two_elements(self):
        self.assertEqual(solve([1, 2]), 1.5)
    
    def test_odd_length_five_elements(self):
        self.assertEqual(solve([1, 5, 7, 10, 11]), 7)
    
    def test_unsorted_array(self):
        self.assertEqual(solve([4, 5, 1]), 4)
    
    def test_with_duplicates(self):
        self.assertEqual(solve([1, 2, 2]), 2)
    
    # Private tests
    def test_all_duplicates(self):
        self.assertEqual(solve([2, 2, 2, 2]), 2)
    
    def test_odd_length_seven_elements(self):
        self.assertEqual(solve([1, 3, 3, 6, 7, 8, 9]), 6)
    
    def test_large_numbers(self):
        self.assertEqual(solve([1000000, 2000000, 3000000]), 2000000)
    
    def test_even_length_with_zero(self):
        self.assertEqual(solve([3, 7, 8, 0]), 5)
    
    def test_even_length_unsorted(self):
        self.assertEqual(solve([4, 7, 8, 1]), 5.5)


if __name__ == "__main__":
    unittest.main()