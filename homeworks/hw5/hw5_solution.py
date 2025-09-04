
def add_ing(s: str) -> str:
    s += 'ing'
    return s


def change_symbol(s: str) -> str:
    s = s.replace('#', '/')
    return s


def change_order(s: str) -> str:
    name = s.split()
    return ' '.join(reversed(name))


def clean_string(s: str) -> str:
    s = s.strip()
    return s


def to_capitalize(s: str) -> str:
    s = s.capitalize()
    return s


def to_list(s: str) -> list:
    arr = s.split()
    return arr


def formatting(array: list, s1: str, s2: str) -> str:
    a = " ".join(array)
    b = "Hello, {a}! {s1} to {s2}".format(a=a, s1=s1, s2=s2)
    return b


def to_string(array: list) -> str:
    arr = " ".join(array)
    return arr


def insert_to_list(array: list, item: int | str, indx: int) -> list:
    array.insert(indx, item)
    return array


def delete_from_list(array: list, indx: int) -> list:
    del array[indx]
    return array
