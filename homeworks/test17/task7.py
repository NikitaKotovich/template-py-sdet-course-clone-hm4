def change_str(string, n):
    a = string[:n]
    return a + a[-2::-1]


S = "abcdef...xyz"
assert change_str(S, 1) == "a"
assert change_str(S, 2) == "aba"
assert change_str(S, 3) == "abcba"
assert change_str(S, 4) == "abcdcba"
