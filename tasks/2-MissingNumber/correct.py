from typing import List


def solve(input_array: List[int]) -> int:
    """
    Находит пропущенное число в последовательности последовательных чисел.
    Возвращает пропущенное число или -1, если пропусков нет или массив пуст.
    """
    if len(input_array) == 0:
        return -1
    
    for i in range(1, len(input_array)):
        if input_array[i] - input_array[i - 1] > 1:
            return input_array[i] - 1
    
    return -1