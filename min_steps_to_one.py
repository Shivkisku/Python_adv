import math

def min_steps_to_1(N):
    if N <= 1:
        return 0

    dp = [float('inf')] * (N + 1)
    dp[1] = 0

    for i in range(2, N + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[max(j, i // j)] + 1)

    return dp[N]

# Example usage:
N = 100
result = min_steps_to_1(N)
print(result)  # Output: 5
