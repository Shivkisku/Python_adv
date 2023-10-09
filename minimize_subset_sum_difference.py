def minimize_subset_sum_difference(nums):
    total_sum = sum(nums)
    n = len(nums)

    # Create a 2D table dp[i][j] where dp[i][j] represents if it's possible
    # to achieve a sum of j with the first i elements.
    dp = [[False for _ in range(total_sum // 2 + 1)] for _ in range(n + 1)]

    # Initialize the first column to True (an empty subset can achieve a sum of 0)
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, total_sum // 2 + 1):
            if j < nums[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

    # Find the largest j such that dp[n][j] is True
    j = total_sum // 2
    while j >= 0 and not dp[n][j]:
        j -= 1

    # Construct one subset based on dp table
    subset1 = []
    i = n
    while i > 0 and j > 0:
        if not dp[i - 1][j]:
            subset1.append(nums[i - 1])
            j -= nums[i - 1]
        i -= 1

    # Construct the other subset by subtracting subset1 from the original array
    subset2 = [num for num in nums if num not in subset1]

    return subset1, subset2

# Example usage:
nums = [5, 10, 15, 20, 25]
subset1, subset2 = minimize_subset_sum_difference(nums)
print("Subset 1:", subset1)
print("Subset 2:", subset2)
