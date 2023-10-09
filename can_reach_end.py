def can_reach_end(nums):
    max_reach = 0
    n = len(nums)

    for i in range(n):
        if i > max_reach:
            return False  # If the current index is unreachable
        max_reach = max(max_reach, i + nums[i])

    return True

# Example usage:
list1 = [2, 0, 1, 0]
result1 = can_reach_end(list1)
print(result1)  # Output: True

list2 = [1, 1, 0, 1]
result2 = can_reach_end(list2)
print(result2)  # Output: False
