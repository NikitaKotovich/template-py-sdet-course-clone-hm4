def number(n):
    return n ** 2


assert number(1) == 1
assert number(2) == 4
assert number(5) == 25
assert number(10) == 100


def checknumber(n):
    if n % 2 == 0:
        return True
    else:
        return False


assert checknumber(2) is True
assert checknumber(5) is False
assert checknumber(888) is True
assert checknumber(12345) is False
