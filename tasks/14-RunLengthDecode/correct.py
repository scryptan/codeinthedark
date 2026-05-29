def solve(input_string: str) -> str:
    result = []
    i = 0

    while i < len(input_string):
        symbol = input_string[i]
        i += 1

        digits = []
        while i < len(input_string) and input_string[i].isdigit():
            digits.append(input_string[i])
            i += 1

        count = int("".join(digits)) if digits else 1
        result.append(symbol * count)

    return "".join(result)
