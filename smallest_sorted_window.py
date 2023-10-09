def findUnsortedWindow(arr):
    n = len(arr)

    # Find the left boundary
    left_boundary = 0
    while left_boundary < n - 1 and arr[left_boundary] <= arr[left_boundary + 1]:
        left_boundary += 1

    if left_boundary == n - 1:
        # The array is already sorted
        return (0, 0)

    # Find the right boundary
    right_boundary = n - 1
    while right_boundary > 0 and arr[right_boundary] >= arr[right_boundary - 1]:
        right_boundary -= 1

    # Find the minimum and maximum values within the unsorted window
    min_val = min(arr[left_boundary:right_boundary + 1])
    max_val = max(arr[left_boundary:right_boundary + 1])

    # Extend the left boundary to the left if there are elements greater than the minimum value
    while left_boundary > 0 and arr[left_boundary - 1] > min_val:
        left_boundary -= 1

    # Extend the right boundary to the right if there are elements smaller than the maximum value
    while right_boundary < n - 1 and arr[right_boundary + 1] < max_val:
        right_boundary += 1

    return (left_boundary, right_boundary)

# Example usage:
if __name__ == "__main__":
    arr = [3, 7, 5, 6, 9]
    result = findUnsortedWindow(arr)
    print(result)  # Output: (1, 3)
