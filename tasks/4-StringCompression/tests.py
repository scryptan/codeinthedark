import unittest
from solution import solve


class StringCompressionTests(unittest.TestCase):
    def assert_case(self, input_string, expected):
        actual = solve(input_string)
        input_display = repr(input_string).replace("\n", "\\n")
        self.assertEqual(
            actual,
            expected,
            f"{input_display} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_empty_string(self):
        self.assert_case("", "")
    
    def test_three_same_chars(self):
        self.assert_case("aaa", "a3")
    
    def test_all_different_chars(self):
        self.assert_case("abc", "abc")
    
    def test_mixed_compression(self):
        self.assert_case("abba", "ab2a")
    
    def test_complex_example(self):
        self.assert_case("aabcccccaaa", "a2bc5a3")
    
    # Private tests
    def test_single_char(self):
        self.assert_case("a", "a")
    
    def test_two_same_chars(self):
        self.assert_case("aa", "a2")
    
    def test_two_different_chars(self):
        self.assert_case("aab", "a2b")
    
    def test_two_pairs(self):
        self.assert_case("aabb", "a2b2")
    
    def test_three_then_one(self):
        self.assert_case("aaab", "a3b")
    
    def test_three_then_two(self):
        self.assert_case("aaabb", "a3b2")
    
    def test_three_and_three(self):
        self.assert_case("aaabbb", "a3b3")
    
    def test_multiple_repetitions(self):
        self.assert_case("hhhhhelllllooooo", "h5el5o5")
    
    def test_uppercase_letters(self):
        self.assert_case("AAABBBCCCD", "A3B3C3D")
    
    def test_spaces(self):
        self.assert_case("   ", " 3")
    
    def test_exclamation_marks(self):
        self.assert_case("!!!!!!!!!!!!", "!12")
    
    def test_single_char_with_long_repetition(self):
        self.assert_case("abbbbbbbbbbbb", "ab12")
    
    def test_complex_word(self):
        self.assert_case("Mississippi", "Mis2is2ip2i")
    
    def test_many_zs(self):
        self.assert_case("zzzzzzzzzzzzzzzzzzzz", "z20")
    
    def test_no_consecutive_repetitions(self):
        self.assert_case("abcabcabc", "abcabcabc")
    
    def test_single_char_again(self):
        self.assert_case("a", "a")
    
    def test_twelve_as(self):
        self.assert_case("aaaaaaaaaaaa", "a12")
    
    def test_string_with_spaces(self):
        self.assert_case("a b c d", "a b c d")


if __name__ == "__main__":
    unittest.main()
