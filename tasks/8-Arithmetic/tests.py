import unittest
from solution import solve


class SumFromXToYTests(unittest.TestCase):
    def assert_case(self, x, y, expected):
        actual = solve(x, y)
        self.assertEqual(
            actual,
            expected,
            f"{x!r} {y!r} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_zero_to_zero(self):
        self.assert_case(0, 0, 0)
    
    def test_one_to_ten(self):
        self.assert_case(1, 10, 55)
    
    def test_two_to_five(self):
        self.assert_case(2, 5, 14)
    
    def test_negative_to_zero(self):
        self.assert_case(-7, 0, -28)
    
    # Private tests
    def test_negative_to_positive(self):
        self.assert_case(-1, 4, 9)


if __name__ == "__main__":
    unittest.main()
