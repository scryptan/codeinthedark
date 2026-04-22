def solve(input_number: int) -> str:
    """
    Классическая задача FizzBuzz.
    - Для чисел, кратных 3 и 5: возвращает "FizzBuzz"
    - Для чисел, кратных 3: возвращает "Fizz"
    - Для чисел, кратных 5: возвращает "Buzz"
    - Иначе: возвращает число в виде строки
    """
    if input_number % 15 == 0:
        return "FizzBuzz"
    
    if input_number % 3 == 0:
        return "Fizz"
    
    if input_number % 5 == 0:
        return "Buzz"
    
    return str(input_number)