def count_char(raw_str: str) -> str:
    if raw_str == "":
        return ""
    raw = ""
    current_char = raw_str[0]
    count = 1
    for i in range(1, len(raw_str)):
        if raw_str[i] == current_char:
            count += 1
        else:
            raw += current_char
            if count > 1:
                raw += str(count)
            current_char = raw_str[i]
            count = 1
    raw += current_char
    if count > 1:
        raw += str(count)
    return raw
