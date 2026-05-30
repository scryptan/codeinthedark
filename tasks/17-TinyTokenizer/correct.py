def solve(prompt: str) -> int:
    tokens = 0
    in_word = False

    for char in prompt:
        if char.isalnum():
            if not in_word:
                tokens += 1
                in_word = True
        elif char.isspace():
            in_word = False
        else:
            tokens += 1
            in_word = False

    return tokens
