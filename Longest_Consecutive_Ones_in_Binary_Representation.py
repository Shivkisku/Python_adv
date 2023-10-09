def longest_consecutive_ones(n):
    binary_str = bin(n)[2:]  # Convert integer to binary and remove the '0b' prefix
    max_count = 0
    current_count = 0

    for char in binary_str:
        if char == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

# Example usage:
n = 156
result = longest_consecutive_ones(n)
print(result)  # Output: 3
