import unittest
from solution import solve


class AsciiFrameTests(unittest.TestCase):
    def assert_case(self, input_int, expected):
        actual = solve(input_int)
        self.assertEqual(
            actual,
            expected,
            f"{input_int!r} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_zero(self):
        self.assert_case(0, [])

    def test_one(self):
        self.assert_case(1, ["#"])

    def test_two(self):
        self.assert_case(2, ["##", "##"])

    def test_three(self):
        self.assert_case(3, ["###", "#.#", "###"])

    def test_five(self):
        self.assert_case(5, ["#####", "#...#", "#...#", "#...#", "#####"])

    # Private tests
    def test_negative(self):
        self.assert_case(-4, [])

    def test_four(self):
        self.assert_case(4, ["####", "#..#", "#..#", "####"])

    def test_six(self):
        self.assert_case(6, ["######", "#....#", "#....#", "#....#", "#....#", "######"])

    def test_seven(self):
        self.assert_case(7, ["#######", "#.....#", "#.....#", "#.....#", "#.....#", "#.....#", "#######"])


if __name__ == "__main__":
    unittest.main()
