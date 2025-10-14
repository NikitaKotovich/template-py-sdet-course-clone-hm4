def sum_to_n(n):
    summ = 0
    for i in range(1, n + 1):
        summ += i
    return summ
assert sum_to_n(1) == 1
assert sum_to_n(2) == 3
assert sum_to_n(8) == 36
assert sum_to_n(22) == 253
assert sum_to_n(100) == 5050