import unittest
from solution import solve


class PalindromeTests(unittest.TestCase):
    # Public tests
    def assert_case(self, input_string: str, expected: bool):
        actual = solve(input_string)
        input_display = repr(input_string).replace("\n", "\\n")
        # Provide a concise case line for the checker output.
        self.assertEqual(
            actual,
            expected,
            f"{input_display} -> expected {expected}, actual {actual}",
        )

    def test_empty_string(self):
        self.assert_case("", True)

    def test_single_char(self):
        self.assert_case("a", True)

    def test_not_palindrome(self):
        self.assert_case("hello world", False)

    def test_simple_palindrome(self):
        self.assert_case("racecar", True)

    def test_ignore_punctuation_and_case(self):
        self.assert_case("A man, a plan, a canal: Panama", True)

    def test_ignore_apostrophes(self):
        self.assert_case("No 'x' in Nixon", True)

    def test_numeric_palindrome_inside(self):
        self.assert_case("n8n", True)

    # Private tests
    def test_another_simple_palindrome(self):
        self.assert_case("madam", True)

    def test_longer_non_palindrome(self):
        self.assert_case("programming", False)

    def test_complex_sentence(self):
        self.assert_case("Was it a car or a cat I saw?", True)

    def test_numeric_palindrome(self):
        self.assert_case("12321", True)

    def test_numeric_non_palindrome(self):
        self.assert_case("12345", False)

    def test_spaces_only(self):
        self.assert_case("   ", True)

    def test_space_between_chars(self):
        self.assert_case("a a", True)

    def test_uppercase_single_char(self):
        self.assert_case("A", True)

    def test_mixed_case_two_chars(self):
        self.assert_case("Aa", True)


if __name__ == "__main__":
    unittest.main()
