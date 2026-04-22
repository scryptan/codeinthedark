from typing import Optional


def solve(input_string: str) -> Optional[str]:
    """
    Находит первый символ, который встречается ровно один раз подряд.
    Возвращает символ или None, если такого символа нет.
    """
    if input_string == "":
        return None
    
    current = input_string[0]
    count = 1
    
    for i in range(1, len(input_string)):
        if input_string[i] != current:
            if count == 1:
                return current
            
            count = 1
            current = input_string[i]
        else:
            count += 1
    
    if count == 1:
        return current
    
    return None