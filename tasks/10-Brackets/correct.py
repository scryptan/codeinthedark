def solve(input_string: str) -> bool:
    """
    Проверяет правильность расстановки круглых скобок.
    Возвращает True, если все скобки правильно сбалансированы, иначе False.
    """
    stack = []
    for c in input_string:
        if c == '(':
            stack.append(c)
        else:  # c == ')'
            if len(stack) == 0:
                return False
            stack.pop()
    
    return len(stack) == 0