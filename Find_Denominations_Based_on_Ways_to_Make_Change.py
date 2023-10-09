def find_denominations(ways_to_make_change):
    denominations = []

    for i, ways in enumerate(ways_to_make_change):
        if ways > 0:
            denominations.append(i)

    return denominations

# Example usage:
ways_to_make_change = [1, 0, 1, 1, 2]
result = find_denominations(ways_to_make_change)
print(result)  # Output: [0, 2, 3, 4]
