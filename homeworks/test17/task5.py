def is_palindrome(num):
    return str(num) == str(num)[::-1]
assert is_palindrome(121) == True
assert is_palindrome(-121) == False
assert is_palindrome(10) == False
assert is_palindrome(0) == True
assert is_palindrome(1001) == True
assert is_palindrome(100) == False
