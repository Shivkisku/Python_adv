def my_reduce(arr, func, initial):
    result = initial
    for element in arr:
        result = func(result, element)
    return result

# Example usage:
def add(a, b):
    return a + b

def product(a, b):
    return a * b

lst = [1, 2, 3, 4, 5]

# Using my_reduce to compute the sum of the list
sum_result = my_reduce(lst, add, 0)
print(sum_result)  # Output: 15

# Using my_reduce to compute the product of the list
product_result = my_reduce(lst, product, 1)
print(product_result)  # Output: 120
