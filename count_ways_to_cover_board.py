def countWaysToCoverBoard(N):
    # Create a list to store the number of ways for each column
    ways = [0] * (N + 1)

    # Initialize the base cases
    ways[0] = 1
    ways[1] = 1

    for i in range(2, N + 1):
        # Calculate the number of ways to cover the current column
        ways[i] = ways[i - 1] + ways[i - 2] * 2

    return ways[N]

# Example usage:
if __name__ == "__main__":
    N = 4
    result = countWaysToCoverBoard(N)
    print(result)  # Output: 11
