def birthday(s, d, m):
    count = 0
    n = len(s)

    for i in range(n - m + 1):
        segment = s[i:i + m]
        if sum(segment) == d:
            count += 1

    return count

# Example usage:
n = 5
squares = [1, 2, 1, 3, 2]
day = 3
month = 2

result = birthday(squares, day, month)
print(result)  # Output: 2
