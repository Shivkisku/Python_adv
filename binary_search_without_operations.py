def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index without multiplication
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_to_find = 6
print(binary_search(sorted_list, element_to_find))  # Output: True
