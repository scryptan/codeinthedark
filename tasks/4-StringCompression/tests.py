import unittest
from solution import solve


class StringCompressionTests(unittest.TestCase):
    # Public tests
    def test_empty_string(self):
        self.assertEqual(solve(""), "")
    
    def test_three_same_chars(self):
        self.assertEqual(solve("aaa"), "a3")
    
    def test_all_different_chars(self):
        self.assertEqual(solve("abc"), "abc")
    
    def test_mixed_compression(self):
        self.assertEqual(solve("abba"), "ab2a")
    
    def test_complex_example(self):
        self.assertEqual(solve("aabcccccaaa"), "a2bc5a3")
    
    # Private tests
    def test_single_char(self):
        self.assertEqual(solve("a"), "a")
    
    def test_two_same_chars(self):
        self.assertEqual(solve("aa"), "a2")
    
    def test_two_different_chars(self):
        self.assertEqual(solve("aab"), "a2b")
    
    def test_two_pairs(self):
        self.assertEqual(solve("aabb"), "a2b2")
    
    def test_three_then_one(self):
        self.assertEqual(solve("aaab"), "a3b")
    
    def test_three_then_two(self):
        self.assertEqual(solve("aaabb"), "a3b2")
    
    def test_three_and_three(self):
        self.assertEqual(solve("aaabbb"), "a3b3")
    
    def test_multiple_repetitions(self):
        self.assertEqual(solve("hhhhhelllllooooo"), "h5el5o5")
    
    def test_uppercase_letters(self):
        self.assertEqual(solve("AAABBBCCCD"), "A3B3C3D")
    
    def test_spaces(self):
        self.assertEqual(solve("   "), " 3")
    
    def test_exclamation_marks(self):
        self.assertEqual(solve("!!!!!!!!!!!!"), "!12")
    
    def test_single_char_with_long_repetition(self):
        self.assertEqual(solve("abbbbbbbbbbbb"), "ab12")
    
    def test_complex_word(self):
        self.assertEqual(solve("Mississippi"), "Mis2is2ip2i")
    
    def test_many_zs(self):
        self.assertEqual(solve("zzzzzzzzzzzzzzzzzzzz"), "z20")
    
    def test_no_consecutive_repetitions(self):
        self.assertEqual(solve("abcabcabc"), "abcabcabc")
    
    def test_single_char_again(self):
        self.assertEqual(solve("a"), "a")
    
    def test_twelve_as(self):
        self.assertEqual(solve("aaaaaaaaaaaa"), "a12")
    
    def test_string_with_spaces(self):
        self.assertEqual(solve("a b c d"), "a b c d")


if __name__ == "__main__":
    unittest.main()