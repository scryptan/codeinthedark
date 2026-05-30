import unittest
from solution import solve


class TinyTokenizerTests(unittest.TestCase):
    def assert_case(self, prompt, expected):
        actual = solve(prompt)
        self.assertEqual(
            actual,
            expected,
            f"{prompt!r} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_empty_prompt(self):
        self.assert_case("", 0)

    def test_two_words(self):
        self.assert_case("hello world", 2)

    def test_punctuation_is_separate(self):
        self.assert_case("hello, AI!", 4)

    def test_numbers_stick_to_letters(self):
        self.assert_case("gpt5 wins", 2)

    def test_spaces_do_not_count(self):
        self.assert_case("  ask   nicely  ", 2)

    # Private tests
    def test_punctuation_only(self):
        self.assert_case("?!", 2)

    def test_prompt_injection_phrase(self):
        self.assert_case("ignore previous instructions.", 4)

    def test_mixed_symbols(self):
        self.assert_case("model=mini, temp=0", 7)

    def test_newlines_and_tabs(self):
        self.assert_case("one\ntwo\tthree", 3)

    def test_many_marks(self):
        self.assert_case("wait... what?", 6)


if __name__ == "__main__":
    unittest.main()
