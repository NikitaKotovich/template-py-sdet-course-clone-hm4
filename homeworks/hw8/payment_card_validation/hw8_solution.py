def is_card_number_valid(number) -> bool:
    card_number = str(number)
    if not card_number:
        return False
    if not card_number.isdigit():
        return False
    card_number = card_number[::-1]
    odd = card_number[::2]
    even = card_number[1::2]
    card = 0
    for i in even:
        doubled = int(i) * 2
        if doubled <= 9:
            card += doubled
        else:
            card += doubled - 9
    for i in odd:
        card += int(i)
    return card % 10 == 0
