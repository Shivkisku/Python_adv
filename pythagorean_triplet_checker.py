def has_pythagorean_triplet(nums):
    n = len(nums)

    # Square all elements in the array
    squared_nums = [x * x for x in nums]

    # Sort the squared_nums in ascending order
    squared_nums.sort()

    # Fix one element and find the other two using two pointers
    for i in range(n - 1, 1, -1):
        left = 0
        right = i - 1
        while left < right:
            if squared_nums[left] + squared_nums[right] == squared_nums[i]:
                return True  # Found a Pythagorean triplet
            elif squared_nums[left] + squared_nums[right] < squared_nums[i]:
                left += 1
            else:
                right -= 1

    return False  # No Pythagorean triplet found

# Example usage:
nums = [3, 1, 4, 6, 5]
print(has_pythagorean_triplet(nums))  
