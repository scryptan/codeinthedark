import unittest
from solution import solve


class FirstUniqueConsecutiveCharTests(unittest.TestCase):
    # Public tests
    def test_empty_string_returns_none(self):
        self.assertIsNone(solve(""))
    
    def test_single_char_returns_that_char(self):
        self.assertEqual(solve("a"), "a")
    
    def test_two_different_chars_returns_first(self):
        self.assertEqual(solve("ab"), "a")
    
    def test_two_same_then_different_returns_last(self):
        self.assertEqual(solve("aab"), "b")
    
    def test_all_same_returns_none(self):
        self.assertIsNone(solve("aaa"))
    
    def test_complex_string(self):
        self.assertEqual(solve("ccaaadhjddsii"), "d")
    
    def test_with_space(self):
        self.assertEqual(solve("ccccccccooooooooddddddee clash"), " ")
    
    # Private tests
    def test_long_string_with_repetitions(self):
        self.assertEqual(solve("aaaaaaabbbbba"), "a")
    
    def test_first_char_unique(self):
        self.assertEqual(solve("ckkko"), "c")
    
    def test_all_same_long(self):
        self.assertIsNone(solve("dddddd"))


if __name__ == "__main__":
    unittest.main()