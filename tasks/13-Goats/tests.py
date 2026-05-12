import unittest
from solution import solve


class GoatsTests(unittest.TestCase):
    def assert_case(self, n, input_array, expected):
        # Convert iterables (e.g. enumerate) to list so they are printable and reusable.
        if not isinstance(input_array, list):
            input_array = list(input_array)

        actual = solve(n, input_array)
        self.assertEqual(
            actual,
            expected,
            f"{n!r} {repr(input_array)} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_basic_case(self):
        self.assert_case(3, [(1, 'R'), (2, 'L')], 2)
    
    def test_all_right(self):
        self.assert_case(3, [(0, 'R'), (1, 'R'), (2, 'R')], 3)
    
    def test_all_left(self):
        self.assert_case(3, [(1, 'L'), (2, 'L'), (3, 'L')], 3)
    
    def test_mixed_1(self):
        self.assert_case(10, [(2, 'L'), (3, 'R'), (8, 'R'), (9, 'R')], 7)
    
    def test_mixed_2(self):
        self.assert_case(3, list(enumerate(['R', 'R', 'L'])), 3)

    # Private tests
    def test_example_LRRRLLL(self):
        self.assert_case(7, list(enumerate(['L', 'R', 'R', 'R', 'L', 'L', 'L'])), 6)
    
    def test_example_RRLLLR(self):
        self.assert_case(6, list(enumerate(['R', 'R', 'L', 'L', 'L', 'R'])), 6)
    
    def test_single_L(self):
        self.assert_case(2, [(1, 'L')], 1)
    
    def test_single_R(self):
        self.assert_case(1, list(enumerate(['R'])), 1)
    
    def test_example_RRRLL(self):
        self.assert_case(19, list(enumerate(['R', 'R', 'R', 'L', 'L'], start=7)), 12)
    
    def test_empty_corridor(self):
        self.assert_case(10, [], 0)
    
    def test_L_at_end(self):
        self.assert_case(5, list(enumerate(['R', 'R', 'R', 'R', 'L'])), 5)
    
    def test_R_at_start(self):
        self.assert_case(5, list(enumerate(['R', 'L', 'L', 'L', 'L'])), 5)
    
    def test_alternating(self):
        self.assert_case(20, list(enumerate(['R', 'L', 'R', 'L', 'R', 'L'], start=2)), 18)
    
    def test_long_sequence(self):
        robots = ['R'] * 50 + ['L'] * 50
        self.assert_case(150, list(enumerate(robots)), 150)
    
    def test_all_L_long(self):
        self.assert_case(200, list(enumerate(['L'] * 100)), 99)
    
    def test_all_R_long(self):
        self.assert_case(300, list(enumerate(['R'] * 100, start=200)), 100)
    
    def test_L_then_R(self):
        self.assert_case(14, list(enumerate(['L', 'L', 'L', 'R', 'R', 'R'])), 11)
    
    def test_mixed_middle(self):
        self.assert_case(13, list(enumerate(['L', 'L', 'L', 'R', 'R', 'L', 'L'])), 10)


if __name__ == "__main__":
    unittest.main()
