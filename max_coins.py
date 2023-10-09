def maxCoinsInMatrix(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])

    # Create a 2D table to store the maximum coins at each cell
    dp = [[0] * cols for _ in range(rows)]

    # Fill in the first row and first column of the table
    dp[0][0] = matrix[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]

    # Fill in the rest of the table using dynamic programming
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    # The bottom-right corner cell contains the maximum coins collected
    return dp[rows-1][cols-1]

# Test the function with your example matrix
matrix = [
    [0, 3, 1, 1],
    [2, 0, 0, 4],
    [1, 5, 3, 1]
]
print(maxCoinsInMatrix(matrix))  # Output: 12
