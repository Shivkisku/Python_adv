def reverse(lst, i, j):
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

def sort_with_reverse(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if lst[j] < lst[min_index]:
                min_index = j
        reverse(lst, i, min_index)

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6]
sort_with_reverse(my_list)
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]
