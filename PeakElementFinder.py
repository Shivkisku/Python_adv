def find_peak_element(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return arr[left]

# Example usage:
arr = [1, 3, 20, 4, 1, 0]
peak = find_peak_element(arr)
print(peak)  # Output: 20
