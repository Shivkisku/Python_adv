def throw_dice(N, faces, total):
    # Create a 2D array to store the number of ways for each total and number of dice
    dp = [[0] * (total + 1) for _ in range(N + 1)]

    # Initialize base case: There's one way to achieve a total of 0 with 0 dice
    dp[0][0] = 1

    for i in range(1, N + 1):
        for j in range(1, total + 1):
            for face in range(1, min(faces, j) + 1):
                dp[i][j] += dp[i - 1][j - face]

    return dp[N][total]

# Example usage:
result = throw_dice(3, 6, 7)
print(result)  # Output: 15
