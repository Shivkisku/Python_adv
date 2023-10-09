def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

# Example usage:
nums = [1, 2, 1, 1, 3, 4, 0]
result = majority_element(nums)
print(result)  # Output: 0
