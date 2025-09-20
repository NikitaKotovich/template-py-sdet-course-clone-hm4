def infinity_loop(left: int, right: int) -> bool:
    while left != right:
        if left > right:
            return True
        left = left + 1
        right = right - 1
    return False
