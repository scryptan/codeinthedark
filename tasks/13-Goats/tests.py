import unittest
from solution import solve


class GoatsTests(unittest.TestCase):
    # Public tests
    def test_basic_case(self):
        self.assertEqual(solve(3, [(1, 'R'), (2, 'L')]), 2)
    
    def test_all_right(self):
        self.assertEqual(solve(3, [(0, 'R'), (1, 'R'), (2, 'R')]), 3)
    
    def test_all_left(self):
        self.assertEqual(solve(3, [(1, 'L'), (2, 'L'), (3, 'L')]), 3)
    
    def test_mixed_1(self):
        self.assertEqual(solve(10, [(2, 'L'), (3, 'R'), (8, 'R'), (9, 'R')]), 7)
    
    def test_mixed_2(self):
        self.assertEqual(solve(3, enumerate(['R', 'R', 'L'])), 3)

    # Private tests
    def test_example_LRRRLLL(self):
        self.assertEqual(solve(7, enumerate(['L', 'R', 'R', 'R', 'L', 'L', 'L'])), 6)
    
    def test_example_RRLLLR(self):
        self.assertEqual(solve(6, enumerate(['R', 'R', 'L', 'L', 'L', 'R'])), 6)
    
    def test_single_L(self):
        self.assertEqual(solve(2, [(1, 'L')]), 1)
    
    def test_single_R(self):
        self.assertEqual(solve(1, enumerate(['R'])), 1)
    
    def test_example_RRRLL(self):
        self.assertEqual(solve(19, enumerate(['R', 'R', 'R', 'L', 'L'], start=7)), 12)
    
    def test_empty_corridor(self):
        self.assertEqual(solve(10, []), 0)
    
    def test_L_at_end(self):
        self.assertEqual(solve(5, enumerate(['R', 'R', 'R', 'R', 'L'])), 5)
    
    def test_R_at_start(self):
        self.assertEqual(solve(5, enumerate(['R', 'L', 'L', 'L', 'L'])), 5)
    
    def test_alternating(self):
        self.assertEqual(solve(20, enumerate(['R', 'L', 'R', 'L', 'R', 'L'], start=2)), 18)
    
    def test_long_sequence(self):
        robots = ['R'] * 50 + ['L'] * 50
        self.assertEqual(solve(150, enumerate(robots)), 150)
    
    def test_all_L_long(self):
        self.assertEqual(solve(200, enumerate(['L'] * 100)), 99)
    
    def test_all_R_long(self):
        self.assertEqual(solve(300, enumerate(['R'] * 100, start=200)), 100)
    
    def test_L_then_R(self):
        self.assertEqual(solve(14, enumerate(['L', 'L', 'L', 'R', 'R', 'R'])), 11)
    
    def test_mixed_middle(self):
        self.assertEqual(solve(13, enumerate(['L', 'L', 'L', 'R', 'R', 'L', 'L'])), 10)


if __name__ == "__main__":
    unittest.main()