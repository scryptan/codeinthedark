import unittest
from solution import solve


class FirstUniqueConsecutiveCharTests(unittest.TestCase):
    def assert_case(self, input_string, expected):
        actual = solve(input_string)
        input_display = repr(input_string).replace("\n", "\\n")
        if expected is None:
            self.assertIsNone(
                actual,
                f"{input_display} -> expected None, actual {actual!r}",
            )
        else:
            self.assertEqual(
                actual,
                expected,
                f"{input_display} -> expected {expected!r}, actual {actual!r}",
            )

    # Public tests
    def test_empty_string_returns_none(self):
        self.assert_case("", None)
    
    def test_single_char_returns_that_char(self):
        self.assert_case("a", "a")
    
    def test_two_different_chars_returns_first(self):
        self.assert_case("ab", "a")
    
    def test_two_same_then_different_returns_last(self):
        self.assert_case("aab", "b")
    
    def test_all_same_returns_none(self):
        self.assert_case("aaa", None)
    
    def test_complex_string(self):
        self.assert_case("ccaaadhjddsii", "d")
    
    def test_with_space(self):
        self.assert_case("ccccccccooooooooddddddee clash", " ")
    
    # Private tests
    def test_long_string_with_repetitions(self):
        self.assert_case("aaaaaaabbbbba", "a")
    
    def test_first_char_unique(self):
        self.assert_case("ckkko", "c")
    
    def test_all_same_long(self):
        self.assert_case("dddddd", None)


if __name__ == "__main__":
    unittest.main()
