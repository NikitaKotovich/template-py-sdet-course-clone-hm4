variable = "123456789012345"
assert variable[0] == "1"
assert variable[-1] == "5"
assert variable[2] == "3"
assert variable[-3] == "3"
assert len(variable) == 15
assert variable[::-1] == "543210987654321"
assert variable[:8] == "12345678"
