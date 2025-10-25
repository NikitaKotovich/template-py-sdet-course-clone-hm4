def is_palindrome(num):
    return str(num) == str(num)[::-1]


assert is_palindrome(121) is True
assert is_palindrome(-121) is False
assert is_palindrome(10) is False
assert is_palindrome(0) is True
assert is_palindrome(1001) is True
assert is_palindrome(100) is False
