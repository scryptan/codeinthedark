import unittest
from solution import solve


class TolkDigestTests(unittest.TestCase):
    def assert_case(self, messages, name, expected):
        actual = solve(messages, name)
        self.assertEqual(
            actual,
            expected,
            f"{messages!r}, {name!r} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_mentions_user(self):
        self.assert_case(
            ["доброе утро", "@anna проверь договор", "созвон в 12"],
            "anna",
            ["@anna проверь договор"],
        )

    def test_important_message(self):
        self.assert_case(
            ["обед?", "срочно нужен счет"],
            "alex",
            ["срочно нужен счет"],
        )

    def test_mention_and_important_message_keep_order(self):
        self.assert_case(
            ["срочно: посмотри саммари", "@kate посмотри вебинар на 2x", "спасибо"],
            "kate",
            ["срочно: посмотри саммари", "@kate посмотри вебинар на 2x"],
        )

    def test_no_matches(self):
        self.assert_case(["привет", "вкс в 15"], "oleg", [])

    # Private tests
    def test_case_is_ignored_for_mentions(self):
        self.assert_case(["@Anna нужен апдейт"], "anna", ["@Anna нужен апдейт"])

    def test_case_is_ignored_for_important_message(self):
        self.assert_case(["СРОЧНО: посмотри саммари"], "ira", ["СРОЧНО: посмотри саммари"])

    def test_message_without_russian_marker_is_ignored(self):
        self.assert_case(["посмотри саммари"], "tom", [])

    def test_both_conditions_once(self):
        self.assert_case(["срочно @mira зайди в Толк"], "mira", ["срочно @mira зайди в Толк"])

    def test_partial_name_without_at_does_not_match(self):
        self.assert_case(["anna проверь чат", "@ann проверь чат"], "anna", [])

    def test_empty_messages(self):
        self.assert_case([], "anna", [])


if __name__ == "__main__":
    unittest.main()
