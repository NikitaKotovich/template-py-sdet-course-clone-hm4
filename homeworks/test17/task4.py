def add_one(numbers):
    for i in range(len(numbers)-1, -1, -1):
        if numbers[i] < 9:
            numbers[i] += 1
            return numbers
        numbers[i] = 0
    return [1] + numbers


assert add_one([9]) == [1, 0]
assert add_one([1, 2, 3]) == [1, 2, 4]
assert add_one([1, 1, 9]) == [1, 2, 0]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
