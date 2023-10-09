def is_fibonacci_number(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

# Example usage:
number_to_check = 5
result = is_fibonacci_number(number_to_check)

if result:
    print(f"{number_to_check} is a Fibonacci number.")
else:
    print(f"{number_to_check} is not a Fibonacci number.")
