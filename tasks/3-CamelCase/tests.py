import unittest
from solution import solve


class CamelToSnakeCaseTests(unittest.TestCase):
    # Public tests
    def test_empty_string(self):
        self.assertEqual(solve(""), "")
    
    def test_single_uppercase(self):
        self.assertEqual(solve("A"), "a")
    
    def test_two_words_camel_case(self):
        self.assertEqual(solve("HelloWorld"), "hello_world")
    
    def test_user_id_example(self):
        self.assertEqual(solve("UserId"), "user_id")
    
    def test_api_with_number(self):
        self.assertEqual(solve("ApiV2Endpoint"), "api_v2_endpoint")
    
    # Private tests
    def test_simple_camel(self):
        self.assertEqual(solve("Simple"), "simple")
    
    def test_no_change_needed(self):
        self.assertEqual(solve("NoChange"), "no_change")


if __name__ == "__main__":
    unittest.main()