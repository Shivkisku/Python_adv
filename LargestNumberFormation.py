def largest_number(arr):
    # Convert numbers to strings and define a custom sorting function
    arr = list(map(str, arr))
    arr.sort(key=lambda x: x*10, reverse=True)  # Sort in decreasing order
    
    return ''.join(arr)

# Test the function
numbers = [10, 7, 76, 415]
result = largest_number(numbers)
print(result)
