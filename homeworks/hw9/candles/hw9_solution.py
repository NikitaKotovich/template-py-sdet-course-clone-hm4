def count_candles(candles: int, leftover: int) -> int:
    count = 0
    other = 0
    for _ in range(candles):
        if candles == 0:
            break
        count += candles
        other += candles
        candles = other // leftover
        other = other % leftover
    return count
