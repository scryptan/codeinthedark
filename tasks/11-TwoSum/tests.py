import unittest
from solution import solve


class TwoSumTests(unittest.TestCase):
    def assert_case(self, input_array, input_int, expected):
        actual = solve(input_array, input_int)
        self.assertEqual(
            actual,
            expected,
            f"{repr(input_array)} {input_int!r} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_basic_case(self):
        self.assert_case([2, 7, 11, 15], 9, [0, 1])
    
    def test_another_case(self):
        self.assert_case([3, 2, 4], 6, [1, 2])
    
    def test_with_zero(self):
        self.assert_case([0, 4, 3, 0], 0, [0, 3])
    
    def test_negative_numbers(self):
        self.assert_case([-1, -2, -3, -4, -5], -8, [2, 4])
    
    def test_minimal(self):
        self.assert_case([1, 2], 3, [0, 1])

    # Private tests
    def test_duplicates(self):
        self.assert_case([3, 3], 6, [0, 1])
    
    def test_large_numbers(self):
        self.assert_case([1000000, 500000, 500000], 1000000, [1, 2])
    
    def test_solution_at_end(self):
        self.assert_case([1, 2, 3, 4, 5, 6], 11, [4, 5])
    
    def test_solution_at_start(self):
        self.assert_case([5, 5, 1, 2], 10, [0, 1])
    
    def test_mixed_order(self):
        self.assert_case([10, -2, 3, 7], 5, [1, 3])


if __name__ == "__main__":
    unittest.main()
