def fewestCoins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else None

# Example usage:
if __name__ == "__main__":
    coins1 = [1, 5, 10]
    amount1 = 56
    result1 = fewestCoins(coins1, amount1)
    print(result1)  # Output: 7

    coins2 = [5, 8]
    amount2 = 15
    result2 = fewestCoins(coins2, amount2)
    print(result2)  # Output: 3
