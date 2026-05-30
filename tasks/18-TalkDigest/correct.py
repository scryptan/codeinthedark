def solve(messages: list[str], name: str) -> list[str]:
    result = []
    mention = "@" + name.lower()

    for message in messages:
        text = message.lower()
        if mention in text or "срочно" in text:
            result.append(message)

    return result
