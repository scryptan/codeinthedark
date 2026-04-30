from typing import List


def solve(input_array: List[int], input_int: int) -> List[int]:
    """
    Вычисляет индексы двух элементов, сумма которых дает искомое число
    """
    if len(input_array) == 0:
        return []
    
    array_dict = {}
    for i in range(input_array):
        array_dict[input_array[i]] = i

    for i in range(input_array):
        r = input_int - input_array[i]
        if r in array_dict:
            return [i, array_dict[r]]
    
    return []