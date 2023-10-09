def count_ways(matrix):
    if not matrix:
        return 0

    n = len(matrix)
    m = len(matrix[0])

    # Create a 2D DP matrix to store the number of ways
    dp = [[0] * m for _ in range(n)]

    # Initialize the top-left corner
    dp[0][0] = 1

    # Fill in the DP matrix
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # If it's an empty space, add ways from above and left
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

    # Return the number of ways to the bottom-right corner
    return dp[n - 1][m - 1]

# Example usage:
matrix = [
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]
]
result = count_ways(matrix)
print(result)  # Output: 2
