def solve(n: int, input_array: list[(int, str)]) -> int:
    max_dist = 0
    for pos, dir in input_array:
        current_dist = pos if dir == 'L' else n - pos
        max_dist = max(current_dist, max_dist)
    return max_dist
