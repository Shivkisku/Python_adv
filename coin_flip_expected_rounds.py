def expected_rounds(n):
    if n == 1:
        return 0
    return 1 + expected_rounds(n - 1)

# Example usage:
n = 100
result = expected_rounds(n)
print(result)
