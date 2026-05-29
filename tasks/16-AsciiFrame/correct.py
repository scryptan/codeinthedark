def solve(input_int: int) -> list[str]:
    if input_int <= 0:
        return []

    if input_int == 1:
        return ["#"]

    result = ["#" * input_int]
    for _ in range(input_int - 2):
        result.append("#" + "." * (input_int - 2) + "#")
    result.append("#" * input_int)
    return result
