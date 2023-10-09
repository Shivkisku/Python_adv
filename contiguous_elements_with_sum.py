def find_contiguous_elements_with_sum(arr, K):
    left, right = 0, 0
    current_sum = 0
    result = []

    while right < len(arr):
        current_sum += arr[right]
        while current_sum > K:
            current_sum -= arr[left]
            left += 1
        if current_sum == K:
            result = arr[left:right + 1]
            break
        right += 1

    return result

# Example usage:
arr = [1, 2, 3, 4, 5]
K = 9
result = find_contiguous_elements_with_sum(arr, K)
print(result)  # Output: [2, 3, 4]
