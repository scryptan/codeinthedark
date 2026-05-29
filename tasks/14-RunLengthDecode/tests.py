import unittest
from solution import solve


class RunLengthDecodeTests(unittest.TestCase):
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

    def test_single_letter(self):
        self.assert_case("a", "a")

    def test_simple_counts(self):
        self.assert_case("a3b2c", "aaabbc")

    def test_digits_larger_than_nine(self):
        self.assert_case("x10", "xxxxxxxxxx")

    def test_mixed_letters_and_counts(self):
        self.assert_case("a2bc3", "aabccc")

    # Private tests
    def test_all_single_letters(self):
        self.assert_case("code", "code")

    def test_multiple_multi_digit_counts(self):
        self.assert_case("z12q2", "zzzzzzzzzzzzqq")

    def test_zero_count(self):
        self.assert_case("a0b3", "bbb")

    def test_symbols_are_allowed(self):
        self.assert_case("#3.2", "###..")

    def test_number_after_last_symbol(self):
        self.assert_case("A1b4", "Abbbb")


if __name__ == "__main__":
    unittest.main()
