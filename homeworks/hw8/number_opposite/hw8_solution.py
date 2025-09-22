def number_opposite(n: int, f_number: int) -> int:
    half = n // 2
    opposite = f_number + half
    if opposite >= n:
        opposite -= n
    return opposite
