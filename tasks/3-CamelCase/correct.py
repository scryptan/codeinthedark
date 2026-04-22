def solve(input_string: str) -> str:
    """
    Преобразует camelCase строку в snake_case.
    Каждая заглавная буква заменяется на нижний регистр с префиксом '_'.
    """
    if input_string == "":
        return ""
    
    result = []
    for c in input_string:
        if c.isupper():
            result.append(f"_{c.lower()}")
        else:
            result.append(c)
    
    return "".join(result)