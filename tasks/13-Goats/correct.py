def solve(input_array: list[str]) -> int:
    min_left = len(input_array)
    max_right = 0
    for i in range(len(input_array)):
        if input_array[i] == 'L' and i < min_left:
            min_left = i
        if input_array[i] == 'R' and i > max_right:
            max_right = i
    return max(len(input_array) - min_left, max_right + 1)
