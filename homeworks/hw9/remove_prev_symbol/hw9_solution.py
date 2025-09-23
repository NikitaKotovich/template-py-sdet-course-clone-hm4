def remove_previous_symbol(raw_str: str) -> str:
    if raw_str == "":
        return ""
    raw = ""
    for i in raw_str:
        if i == "#":
            if raw:
                raw = raw[:-1]
        else:
            raw += i
    return raw
