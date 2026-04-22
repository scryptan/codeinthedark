import unittest
from solution import solve


class FizzBuzzTests(unittest.TestCase):
    # Public tests
    def test_one_returns_one(self):
        self.assertEqual(solve(1), "1")
    
    def test_three_returns_fizz(self):
        self.assertEqual(solve(3), "Fizz")
    
    def test_five_returns_buzz(self):
        self.assertEqual(solve(5), "Buzz")
    
    def test_fifteen_returns_fizzbuzz(self):
        self.assertEqual(solve(15), "FizzBuzz")
    
    # Private tests
    def test_zero_returns_fizzbuzz(self):
        self.assertEqual(solve(0), "FizzBuzz")
    
    def test_negative_three_returns_fizz(self):
        self.assertEqual(solve(-3), "Fizz")
    
    def test_negative_five_returns_buzz(self):
        self.assertEqual(solve(-5), "Buzz")
    
    def test_negative_fifteen_returns_fizzbuzz(self):
        self.assertEqual(solve(-15), "FizzBuzz")
    
    def test_six_returns_fizz(self):
        self.assertEqual(solve(6), "Fizz")
    
    def test_nine_returns_fizz(self):
        self.assertEqual(solve(9), "Fizz")
    
    def test_twelve_returns_fizz(self):
        self.assertEqual(solve(12), "Fizz")
    
    def test_ten_returns_buzz(self):
        self.assertEqual(solve(10), "Buzz")
    
    def test_twenty_returns_buzz(self):
        self.assertEqual(solve(20), "Buzz")
    
    def test_twenty_five_returns_buzz(self):
        self.assertEqual(solve(25), "Buzz")
    
    def test_thirty_returns_fizzbuzz(self):
        self.assertEqual(solve(30), "FizzBuzz")
    
    def test_forty_five_returns_fizzbuzz(self):
        self.assertEqual(solve(45), "FizzBuzz")
    
    def test_sixty_returns_fizzbuzz(self):
        self.assertEqual(solve(60), "FizzBuzz")
    
    def test_two_returns_two(self):
        self.assertEqual(solve(2), "2")
    
    def test_four_returns_four(self):
        self.assertEqual(solve(4), "4")
    
    def test_seven_returns_seven(self):
        self.assertEqual(solve(7), "7")
    
    def test_eight_returns_eight(self):
        self.assertEqual(solve(8), "8")
    
    def test_eleven_returns_eleven(self):
        self.assertEqual(solve(11), "11")
    
    def test_thirteen_returns_thirteen(self):
        self.assertEqual(solve(13), "13")
    
    def test_fourteen_returns_fourteen(self):
        self.assertEqual(solve(14), "14")
    
    def test_sixteen_returns_sixteen(self):
        self.assertEqual(solve(16), "16")
    
    def test_seventeen_returns_seventeen(self):
        self.assertEqual(solve(17), "17")
    
    def test_nineteen_returns_nineteen(self):
        self.assertEqual(solve(19), "19")
    
    def test_ninety_nine_returns_fizz(self):
        self.assertEqual(solve(99), "Fizz")
    
    def test_one_hundred_returns_buzz(self):
        self.assertEqual(solve(100), "Buzz")
    
    def test_one_hundred_five_returns_fizzbuzz(self):
        self.assertEqual(solve(105), "FizzBuzz")


if __name__ == "__main__":
    unittest.main()