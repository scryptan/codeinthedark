import unittest
from solution import solve


class ParenthesesBalanceTests(unittest.TestCase):
    # Public tests
    def test_simple_valid(self):
        self.assertTrue(solve("()"))
    
    def test_empty_string(self):
        self.assertTrue(solve(""))
    
    def test_extra_closing(self):
        self.assertFalse(solve("())"))
    
    def test_missing_closing(self):
        self.assertFalse(solve("(()"))
    
    def test_two_pairs(self):
        self.assertTrue(solve("()()"))
    
    def test_nested(self):
        self.assertTrue(solve("(())"))
    
    def test_closing_before_opening(self):
        self.assertFalse(solve(")("))
    
    def test_complex_nested(self):
        self.assertTrue(solve("(()())"))
    
    # Private tests
    def test_deeply_nested(self):
        self.assertTrue(solve("((()))"))
    
    def test_combination(self):
        self.assertTrue(solve("()(())"))
    
    def test_missing_closing_deep(self):
        self.assertFalse(solve("((())"))
    
    def test_extra_closing_middle(self):
        self.assertFalse(solve("())()"))
    
    def test_complex_structure(self):
        self.assertTrue(solve("((()()))"))
    
    def test_starts_with_closing(self):
        self.assertFalse(solve(")(()"))
    
    def test_composite_sequence(self):
        self.assertTrue(solve("()((()))"))
    
    def test_extra_closing_at_end(self):
        self.assertFalse(solve("(()))"))


if __name__ == "__main__":
    unittest.main()