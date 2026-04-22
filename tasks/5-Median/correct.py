from typing import List


def solve(input_array: List[int]) -> float:
    """
    Находит медиану массива чисел.
    Для пустого массива возвращает -1.
    """
    if len(input_array) == 0:
        return -1
    
    ordered = sorted(input_array)
    length = len(ordered)
    
    if length % 2 == 1:
        # Нечетное количество элементов - возвращаем средний
        return float(ordered[length // 2])
    else:
        # Четное количество элементов - среднее арифметическое двух центральных
        return (ordered[length // 2 - 1] + ordered[length // 2]) / 2