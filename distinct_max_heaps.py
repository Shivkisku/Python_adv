def calculate_binomial_coefficient(n, k):
    # Calculate the binomial coefficient (n choose k)
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

def count_max_heaps(arr):
    n = len(arr)
    if n <= 2:
        return 1  # Only one max heap possible for 0, 1, or 2 elements

    # Calculate the height of the heap
    height = 0
    while 2 ** height <= n:
        height += 1
    height -= 1  # Height of the heap

    # Calculate the number of elements in the last level
    last_level = n - (2 ** height) + 1

    # Calculate the number of elements in left and right subtrees
    elements_in_left = min(last_level, 2 ** (height - 1))

    # Calculate the number of max heaps for left and right subtrees
    left_subtree_heaps = calculate_binomial_coefficient(n - 1, elements_in_left - 1)
    right_subtree_heaps = count_max_heaps(arr[:elements_in_left]) * count_max_heaps(arr[elements_in_left + 1:])

    # Total number of max heaps for the current tree
    total_heaps = left_subtree_heaps * right_subtree_heaps * calculate_binomial_coefficient(n - 1, elements_in_left)

    return total_heaps

# Example usage:
arr = [1, 2, 3]
num_ways = count_max_heaps(arr)
print(f"Number of distinct max heaps: {num_ways}")
