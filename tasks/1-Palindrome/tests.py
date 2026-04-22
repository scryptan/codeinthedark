import unittest
from solution import solve


class PalindromeTests(unittest.TestCase):
    # Public tests
    def test_empty_string(self):
        self.assertTrue(solve(""))

    def test_single_char(self):
        self.assertTrue(solve("a"))

    def test_not_palindrome(self):
        self.assertFalse(solve("hello world"))

    def test_simple_palindrome(self):
        self.assertTrue(solve("racecar"))

    def test_ignore_punctuation_and_case(self):
        self.assertTrue(solve("A man, a plan, a canal: Panama"))

    def test_ignore_apostrophes(self):
        self.assertTrue(solve("No 'x' in Nixon"))

    def test_numeric_palindrome_inside(self):
        self.assertTrue(solve("n8n"))

    # Private tests
    def test_another_simple_palindrome(self):
        self.assertTrue(solve("madam"))

    def test_longer_non_palindrome(self):
        self.assertFalse(solve("programming"))

    def test_complex_sentence(self):
        self.assertTrue(solve("Was it a car or a cat I saw?"))

    def test_numeric_palindrome(self):
        self.assertTrue(solve("12321"))

    def test_numeric_non_palindrome(self):
        self.assertFalse(solve("12345"))

    def test_spaces_only(self):
        self.assertTrue(solve("   "))

    def test_space_between_chars(self):
        self.assertTrue(solve("a a"))

    def test_uppercase_single_char(self):
        self.assertTrue(solve("A"))

    def test_mixed_case_two_chars(self):
        self.assertTrue(solve("Aa"))


if __name__ == "__main__":
    unittest.main()