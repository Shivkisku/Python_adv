def divide(product, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")

    if product == 0:
        return (0, 0)

    # Determine the sign of the result
    negative = (product < 0) ^ (divisor < 0)

    # Make both numbers positive to simplify the logic
    product = abs(product)
    divisor = abs(divisor)

    quotient = 0
    while product >= divisor:
        product -= divisor
        quotient += 1

    if negative:
        quotient = -quotient

    return (quotient, product)

# Test cases
print(divide(10, 3))  # Output: (3, 1)
print(divide(7, -3))  # Output: (-2, 1)
print(divide(-10, 2))  # Output: (-5, 0)
