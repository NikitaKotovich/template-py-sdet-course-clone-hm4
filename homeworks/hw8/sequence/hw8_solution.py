def ascending_sequence(arr: list) -> bool:
    count = 0
    for i in range(len(arr) - 1):
        current_int = arr[i]
        next_int = arr[i + 1]
        if current_int > next_int:
            count += 1
            if count >= 1:
                return False
        elif i > 0:
            previous_int = arr[i - 1]
            if previous_int >= next_int:
                return False
    return True
