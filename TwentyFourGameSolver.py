def game24(nums):
    if len(nums) == 1:
        return abs(nums[0] - 24) < 1e-6  # Check if the result is close to 24 (floating-point tolerance)
    
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                
                # Try all four possible operations
                for op in ['+', '-', '*', '/']:
                    if (op == '+' or op == '*') and i > j:
                        continue  # Avoid duplicate calculations for commutative operations
                    if op == '/' and nums[j] == 0:
                        continue  # Avoid division by zero
                    
                    if op == '+':
                        new_nums.append(nums[i] + nums[j])
                    elif op == '-':
                        new_nums.append(nums[i] - nums[j])
                    elif op == '*':
                        new_nums.append(nums[i] * nums[j])
                    elif op == '/':
                        new_nums.append(nums[i] / nums[j])
                    
                    # Recursively check if it's possible to reach 24 with the new list
                    if game24(new_nums):
                        return True
                    
                    new_nums.pop()  # Backtrack

    return False

# Test the game24 function
nums = [5, 2, 7, 8]
result = game24(nums)
print(result)  # Output: True
