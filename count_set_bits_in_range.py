def count_set_bits(n):
    total_set_bits = 0

    for i in range(1, n + 1):
        num = i
        while num > 0:
            total_set_bits += num & 1
            num >>= 1

    return total_set_bits

# Example usage:
N = 10  # Count set bits in integers from 1 to 10
result = count_set_bits(N)
print(result)  # Output: 17
