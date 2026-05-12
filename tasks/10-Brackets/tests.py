import unittest
from solution import solve


class ParenthesesBalanceTests(unittest.TestCase):
    def assert_case(self, input_string, expected: bool):
        actual = solve(input_string)
        input_display = repr(input_string).replace("\n", "\\n")
        self.assertEqual(
            actual,
            expected,
            f"{input_display} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_simple_valid(self):
        self.assert_case("()", True)
    
    def test_empty_string(self):
        self.assert_case("", True)
    
    def test_extra_closing(self):
        self.assert_case("())", False)
    
    def test_missing_closing(self):
        self.assert_case("(()", False)
    
    def test_two_pairs(self):
        self.assert_case("()()", True)
    
    def test_nested(self):
        self.assert_case("(())", True)
    
    def test_closing_before_opening(self):
        self.assert_case(")(", False)
    
    def test_complex_nested(self):
        self.assert_case("(()())", True)
    
    # Private tests
    def test_deeply_nested(self):
        self.assert_case("((()))", True)
    
    def test_combination(self):
        self.assert_case("()(())", True)
    
    def test_missing_closing_deep(self):
        self.assert_case("((())", False)
    
    def test_extra_closing_middle(self):
        self.assert_case("())()", False)
    
    def test_complex_structure(self):
        self.assert_case("((()()))", True)
    
    def test_starts_with_closing(self):
        self.assert_case(")(()", False)
    
    def test_composite_sequence(self):
        self.assert_case("()((()))", True)
    
    def test_extra_closing_at_end(self):
        self.assert_case("(()))", False)


if __name__ == "__main__":
    unittest.main()
