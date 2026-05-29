import unittest
from solution import solve


class RotateLeftTests(unittest.TestCase):
    def assert_case(self, input_array, input_int, expected):
        actual = solve(input_array, input_int)
        self.assertEqual(
            actual,
            expected,
            f"{repr(input_array)} {input_int!r} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_empty_array(self):
        self.assert_case([], 3, [])

    def test_zero_shift(self):
        self.assert_case([1, 2, 3], 0, [1, 2, 3])

    def test_shift_by_one(self):
        self.assert_case([1, 2, 3, 4], 1, [2, 3, 4, 1])

    def test_shift_by_two(self):
        self.assert_case([10, 20, 30, 40, 50], 2, [30, 40, 50, 10, 20])

    def test_shift_larger_than_length(self):
        self.assert_case([1, 2, 3], 5, [3, 1, 2])

    # Private tests
    def test_shift_equal_to_length(self):
        self.assert_case([7, 8, 9], 3, [7, 8, 9])

    def test_single_element(self):
        self.assert_case([42], 100, [42])

    def test_negative_numbers(self):
        self.assert_case([-1, -2, -3, -4], 3, [-4, -1, -2, -3])

    def test_repeated_values(self):
        self.assert_case([5, 5, 1, 2], 2, [1, 2, 5, 5])

    def test_large_shift(self):
        self.assert_case([0, 1, 2, 3, 4, 5], 14, [2, 3, 4, 5, 0, 1])


if __name__ == "__main__":
    unittest.main()
