def change_str(s, n):
    a = s[:n]
    return a + a[-2::-1]


s = "abcdef...xyz"
assert change_str(s, 1) == "a"
assert change_str(s, 2) == "aba"
assert change_str(s, 3) == "abcba"
assert change_str(s, 4) == "abcdcba"
