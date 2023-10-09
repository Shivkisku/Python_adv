def find_maximum(a, b):
    # Calculate the absolute difference between a and b
    diff = a - b

    # Calculate the sign of the difference (1 if positive, 0 if zero, -1 if negative)
    sign = (diff >> 31) & 0x01

    # Use the sign to determine the maximum
    maximum = a - sign * diff

    return maximum

# Example usage:
num1 = 5
num2 = 8
result = find_maximum(num1, num2)
print("Maximum:", result)  # Output: Maximum: 8
