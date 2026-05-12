import unittest
from solution import solve


class CamelToSnakeCaseTests(unittest.TestCase):
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
    
    def test_single_uppercase(self):
        self.assert_case("A", "a")
    
    def test_two_words_camel_case(self):
        self.assert_case("HelloWorld", "hello_world")
    
    def test_user_id_example(self):
        self.assert_case("UserId", "user_id")
    
    def test_api_with_number(self):
        self.assert_case("ApiV2Endpoint", "api_v2_endpoint")
    
    # Private tests
    def test_simple_camel(self):
        self.assert_case("Simple", "simple")
    
    def test_no_change_needed(self):
        self.assert_case("NoChange", "no_change")


if __name__ == "__main__":
    unittest.main()
