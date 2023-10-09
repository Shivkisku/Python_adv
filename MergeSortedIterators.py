def merge_iterators(iter1, iter2):
    # Get the first values from both iterators
    val1 = next(iter1, None)
    val2 = next(iter2, None)
    
    while val1 is not None and val2 is not None:
        if val1 < val2:
            yield val1
            val1 = next(iter1, None)
        else:
            yield val2
            val2 = next(iter2, None)
    
    # Yield any remaining values from both iterators
    while val1 is not None:
        yield val1
        val1 = next(iter1, None)
    
    while val2 is not None:
        yield val2
        val2 = next(iter2, None)

# Example usage:
foo = iter([5, 10, 15])
bar = iter([3, 8, 9])

for num in merge_iterators(foo, bar):
    print(num)
