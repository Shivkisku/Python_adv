def next_permutation(nums):
    n = len(nums)
    
    # Find the first pair of adjacent digits where nums[i] < nums[i+1]
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i == -1:
        # If there's no such pair, reverse the list
        nums.reverse()
        return nums

    # Find the first digit greater than nums[i]
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1

    # Swap nums[i] and nums[j]
    nums[i], nums[j] = nums[j], nums[i]

    # Reverse the portion of the list to the right of index i
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

# Example usage:
nums1 = [1, 2, 3]
nums2 = [1, 3, 2]
nums3 = [3, 2, 1]

print(next_permutation(nums1))  # Output: [1, 3, 2]
print(next_permutation(nums2))  # Output: [2, 1, 3]
print(next_permutation(nums3))  # Output: [1, 2, 3]
