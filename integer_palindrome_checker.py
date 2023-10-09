def is_palindrome(x):
    if x < 0:
        return False  # Negative numbers are not palindromes

    original_x, reversed_x = x, 0
    while x > 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10

    return original_x == reversed_x

# Example usage:
print(is_palindrome(121))  # Output: True
print(is_palindrome(888))  # Output: True
print(is_palindrome(678))  # Output: False
