from typing import List


def solve(input_array: List[int]) -> List[int]:
    """
    Вычисляет префиксное произведение массива.
    Каждый элемент результата - произведение всех предыдущих элементов (включая текущий).
    """
    if len(input_array) == 0:
        return []
    
    result = [0] * len(input_array)
    current = input_array[0]
    result[0] = current
    
    for i in range(1, len(input_array)):
        result[i] = result[i - 1] * input_array[i]
    
    return result