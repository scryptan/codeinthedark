import unittest
from solution import solve


class MissingNumberTests(unittest.TestCase):
    def assert_case(self, input_array, expected):
        actual = solve(input_array)
        self.assertEqual(
            actual,
            expected,
            f"{repr(input_array)} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_missing_2_between_1_and_3(self):
        self.assert_case([1, 3, 4, 5], 2)
    
    def test_missing_4_between_3_and_5(self):
        self.assert_case([1, 2, 3, 5], 4)
    
    def test_no_missing_with_gap_at_end(self):
        self.assert_case([2, 3, 4, 5], -1)
    
    def test_no_missing_sequential(self):
        self.assert_case([1, 2, 3, 4], -1)
    
    def test_empty_array(self):
        self.assert_case([], -1)
    
    # Private tests
    def test_missing_between_two_numbers(self):
        self.assert_case([333, 335], 334)


if __name__ == "__main__":
    unittest.main()
