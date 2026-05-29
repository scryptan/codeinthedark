def solve(input_array: list[int], input_int: int) -> list[int]:
    if not input_array:
        return []

    shift = input_int % len(input_array)
    return input_array[shift:] + input_array[:shift]
