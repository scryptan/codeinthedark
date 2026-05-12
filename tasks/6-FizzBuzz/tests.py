import unittest
from solution import solve


class FizzBuzzTests(unittest.TestCase):
    def assert_case(self, input_number, expected):
        actual = solve(input_number)
        self.assertEqual(
            actual,
            expected,
            f"{input_number!r} -> expected {expected!r}, actual {actual!r}",
        )

    # Public tests
    def test_one_returns_one(self):
        self.assert_case(1, "1")
    
    def test_three_returns_fizz(self):
        self.assert_case(3, "Fizz")
    
    def test_five_returns_buzz(self):
        self.assert_case(5, "Buzz")
    
    def test_fifteen_returns_fizzbuzz(self):
        self.assert_case(15, "FizzBuzz")
    
    # Private tests
    def test_zero_returns_fizzbuzz(self):
        self.assert_case(0, "FizzBuzz")
    
    def test_negative_three_returns_fizz(self):
        self.assert_case(-3, "Fizz")
    
    def test_negative_five_returns_buzz(self):
        self.assert_case(-5, "Buzz")
    
    def test_negative_fifteen_returns_fizzbuzz(self):
        self.assert_case(-15, "FizzBuzz")
    
    def test_six_returns_fizz(self):
        self.assert_case(6, "Fizz")
    
    def test_nine_returns_fizz(self):
        self.assert_case(9, "Fizz")
    
    def test_twelve_returns_fizz(self):
        self.assert_case(12, "Fizz")
    
    def test_ten_returns_buzz(self):
        self.assert_case(10, "Buzz")
    
    def test_twenty_returns_buzz(self):
        self.assert_case(20, "Buzz")
    
    def test_twenty_five_returns_buzz(self):
        self.assert_case(25, "Buzz")
    
    def test_thirty_returns_fizzbuzz(self):
        self.assert_case(30, "FizzBuzz")
    
    def test_forty_five_returns_fizzbuzz(self):
        self.assert_case(45, "FizzBuzz")
    
    def test_sixty_returns_fizzbuzz(self):
        self.assert_case(60, "FizzBuzz")
    
    def test_two_returns_two(self):
        self.assert_case(2, "2")
    
    def test_four_returns_four(self):
        self.assert_case(4, "4")
    
    def test_seven_returns_seven(self):
        self.assert_case(7, "7")
    
    def test_eight_returns_eight(self):
        self.assert_case(8, "8")
    
    def test_eleven_returns_eleven(self):
        self.assert_case(11, "11")
    
    def test_thirteen_returns_thirteen(self):
        self.assert_case(13, "13")
    
    def test_fourteen_returns_fourteen(self):
        self.assert_case(14, "14")
    
    def test_sixteen_returns_sixteen(self):
        self.assert_case(16, "16")
    
    def test_seventeen_returns_seventeen(self):
        self.assert_case(17, "17")
    
    def test_nineteen_returns_nineteen(self):
        self.assert_case(19, "19")
    
    def test_ninety_nine_returns_fizz(self):
        self.assert_case(99, "Fizz")
    
    def test_one_hundred_returns_buzz(self):
        self.assert_case(100, "Buzz")
    
    def test_one_hundred_five_returns_fizzbuzz(self):
        self.assert_case(105, "FizzBuzz")


if __name__ == "__main__":
    unittest.main()
