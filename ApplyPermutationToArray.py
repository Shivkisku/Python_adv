def apply_permutation(arr, permutation):
    if len(arr) != len(permutation):
        raise ValueError("Array and permutation must have the same length.")
    
    result = [None] * len(arr)
    for i, index in enumerate(permutation):
        result[index] = arr[i]
    
    return result

# Test the function
original_array = ["a", "b", "c"]
permutation = [2, 1, 0]
result = apply_permutation(original_array, permutation)
print(result)
