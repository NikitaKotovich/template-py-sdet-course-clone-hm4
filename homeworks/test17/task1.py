VARIABLE = "123456789012345"
assert VARIABLE[0] == "1"
assert VARIABLE[-1] == "5"
assert VARIABLE[2] == "3"
assert VARIABLE[-3] == "3"
assert len(VARIABLE) == 15
assert VARIABLE[::-1] == "543210987654321"
assert VARIABLE[:8] == "12345678"
