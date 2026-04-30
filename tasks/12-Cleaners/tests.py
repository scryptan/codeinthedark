import unittest
from solution import solve


class CleanersTests(unittest.TestCase):
    # Public tests
    def test_basic_case(self):
        self.assertEqual(solve(['R', 'L']), 1)
    
    def test_all_right(self):
        self.assertEqual(solve(['R', 'R', 'R']), 0)
    
    def test_all_left(self):
        self.assertEqual(solve(['L', 'L', 'L']), 0)
    
    def test_mixed_1(self):
        self.assertEqual(solve(['R', 'L', 'L']), 1)
    
    def test_mixed_2(self):
        self.assertEqual(solve(['L', 'R', 'R']), 0)

    # Private tests
    def test_multiple_collisions(self):
        self.assertEqual(solve(['R', 'R', 'L', 'L']), 2)
    
    def test_complex_pattern(self):
        self.assertEqual(solve(['R', 'L', 'R', 'L']), 2)
    
    def test_long_sequence(self):
        self.assertEqual(solve(['R', 'R', 'R', 'L', 'L', 'L']), 3)
    
    def test_single_robot(self):
        self.assertEqual(solve(['R']), 0)
        self.assertEqual(solve(['L']), 0)
    
    def test_empty_corridor(self):
        self.assertEqual(solve([]), 0)
    
    def test_alternating(self):
        self.assertEqual(solve(['R', 'L', 'R', 'L', 'R', 'L']), 3)
    
    def test_left_at_start(self):
        self.assertEqual(solve(['L', 'R', 'R', 'R']), 0)
    
    def test_right_at_end(self):
        self.assertEqual(solve(['R', 'R', 'R', 'L']), 1)
    
    def test_many_robots(self):
        robots = ['R'] * 50 + ['L'] * 50
        self.assertEqual(solve(robots), 2500)


if __name__ == "__main__":
    unittest.main()