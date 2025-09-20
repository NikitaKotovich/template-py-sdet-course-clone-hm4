def missing_statues(arr: list) -> int:
    if not arr:
        return 0
    arr = sorted(set(arr))
    return max(arr) - min(arr) + 1 - len(arr)
