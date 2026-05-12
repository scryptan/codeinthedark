import unittest
from solution import solve


class CleanersTests(unittest.TestCase):
    def assert_case(self, input_array, expected):
        actual = solve(input_array)
        self.assertEqual(
            actual,
            expected,
            f"{repr(input_array)} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_basic_case(self):
        self.assert_case(['R', 'L'], 1)
    
    def test_all_right(self):
        self.assert_case(['R', 'R', 'R'], 0)
    
    def test_all_left(self):
        self.assert_case(['L', 'L', 'L'], 0)
    
    def test_mixed_1(self):
        self.assert_case(['R', 'L', 'L'], 2)
    
    def test_mixed_2(self):
        self.assert_case(['L', 'R', 'R'], 0)

    # Private tests
    def test_multiple_collisions(self):
        self.assert_case(['R', 'R', 'L', 'L'], 4)
    
    def test_complex_pattern(self):
        self.assert_case(['R', 'L', 'R', 'L'], 3)
    
    def test_long_sequence(self):
        self.assert_case(['R', 'R', 'R', 'L', 'L', 'L'], 9)
    
    def test_single_robot(self):
        self.assert_case(['R'], 0)
        self.assert_case(['L'], 0)
    
    def test_empty_corridor(self):
        self.assert_case([], 0)
    
    def test_alternating(self):
        self.assert_case(['R', 'L', 'R', 'L', 'R', 'L'], 6)
    
    def test_left_at_start(self):
        self.assert_case(['L', 'R', 'R', 'R'], 0)
    
    def test_right_at_end(self):
        self.assert_case(['R', 'R', 'R', 'L'], 3)
    
    def test_many_robots(self):
        robots = ['R'] * 50 + ['L'] * 50
        self.assert_case(robots, 2500)


if __name__ == "__main__":
    unittest.main()
