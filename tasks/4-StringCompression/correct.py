def solve(input_string: str) -> str:
    """
    Выполняет сжатие строки: каждый символ заменяется на символ и количество его повторений.
    Если символ встречается 1 раз, число не добавляется.
    """
    if input_string == "":
        return ""
    
    current_symbol = input_string[0]
    count = 1
    result = []
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_symbol:
            count += 1
        else:
            result.append(f"{current_symbol}{_compress(count)}")
            current_symbol = input_string[i]
            count = 1
    
    result.append(f"{current_symbol}{_compress(count)}")
    return "".join(result)


def _compress(count: int) -> str:
    """Возвращает строку с числом, если count > 1, иначе пустую строку"""
    return str(count) if count > 1 else ""