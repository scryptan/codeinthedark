def solve(input_string: str) -> bool:
    filtered = [c.lower() for c in input_string if c.isalnum()]
    return filtered == filtered[::-1]