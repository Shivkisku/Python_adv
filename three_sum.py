def has_three_sum(arr, k):
    arr.sort()  # Sort the array in ascending order
    n = len(arr)

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == k:
                return True  # Found a triplet that adds up to k
            elif current_sum < k:
                left += 1
            else:
                right -= 1

    return False  # No triplet found

# Example usage:
arr = [20, 303, 3, 4, 25]
k = 49
result = has_three_sum(arr, k)
print(result)  # Output: True (20 + 4 + 25 = 49)
