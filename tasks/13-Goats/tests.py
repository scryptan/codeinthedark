import unittest
from solution import solve


class GoatsTests(unittest.TestCase):
    # Public tests
    def test_basic_case(self):
        self.assertEqual(solve(['R', 'L']), 2)
    
    def test_all_right(self):
        self.assertEqual(solve(['R', 'R', 'R']), 3)
    
    def test_all_left(self):
        self.assertEqual(solve(['L', 'L', 'L']), 3)
    
    def test_mixed_1(self):
        self.assertEqual(solve(['L', 'R', 'R', 'R']), 3)
    
    def test_mixed_2(self):
        self.assertEqual(solve(['R', 'R', 'L']), 3)

    # Private tests
    def test_example_LRRRLLL(self):
        self.assertEqual(solve(['L', 'R', 'R', 'R', 'L', 'L', 'L']), 7)
    
    def test_example_RRLLLR(self):
        self.assertEqual(solve(['R', 'R', 'L', 'L', 'L', 'R']), 6)
    
    def test_single_L(self):
        self.assertEqual(solve(['L']), 1)
    
    def test_single_R(self):
        self.assertEqual(solve(['R']), 1)
    
    def test_example_RRRLL(self):
        self.assertEqual(solve(['R', 'R', 'R', 'L', 'L']), 3)
    
    def test_empty_corridor(self):
        self.assertEqual(solve([]), 0)
    
    def test_L_at_end(self):
        self.assertEqual(solve(['R', 'R', 'R', 'R', 'L']), 5)
    
    def test_R_at_start(self):
        self.assertEqual(solve(['R', 'L', 'L', 'L', 'L']), 5)
    
    def test_alternating(self):
        self.assertEqual(solve(['R', 'L', 'R', 'L', 'R', 'L']), 5)
    
    def test_long_sequence(self):
        robots = ['R'] * 50 + ['L'] * 50
        self.assertEqual(solve(robots), 51)
    
    def test_all_L_long(self):
        self.assertEqual(solve(['L'] * 100), 100)
    
    def test_all_R_long(self):
        self.assertEqual(solve(['R'] * 100), 100)
    
    def test_L_then_R(self):
        self.assertEqual(solve(['L', 'L', 'L', 'R', 'R', 'R']), 6)
    
    def test_mixed_middle(self):
        self.assertEqual(solve(['R', 'L', 'L', 'R', 'R', 'L', 'L']), 5)


if __name__ == "__main__":
    unittest.main()