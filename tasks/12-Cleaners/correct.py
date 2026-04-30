def solve(input_array: list[str]) -> int:
    to_the_right = [0]

    for i, dir in enumerate(input_array):
        right_count = to_the_right[-1]
        if dir == 'R':
            right_count += 1
        to_the_right.append(right_count)
    
    collisions_count = 0
    for i, dir in enumerate(input_array):
        if dir == 'L':
            collisions_count += to_the_right[i]

    return collisions_count
