import unittest

from solution import solve


class PalindromeTests(unittest.TestCase):
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

    def test_numeric_palindrome(self):
        self.assertTrue(solve("12321"))

    def test_numeric_non_palindrome(self):
        self.assertFalse(solve("12345"))

    def test_spaces_only(self):
        self.assertTrue(solve("   "))


if __name__ == "__main__":
    unittest.main()
