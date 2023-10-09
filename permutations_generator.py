def permute(nums):
    def backtrack(first):
        if first == len(nums):
            result.append(nums[:])
            return
        for i in range(first, len(nums)):
            nums[first], nums[i] = nums[i], nums[first]
            backtrack(first + 1)
            nums[first], nums[i] = nums[i], nums[first]  # Backtrack

    result = []
    backtrack(0)
    return result

# Example usage:
input_nums = [1, 2, 3]
permutations = permute(input_nums)
print(permutations)
