def min_swaps_to_rearrange_couples(row):
    couple_to_index = {}  # Store the index of each couple
    swaps = 0

    for i, couple in enumerate(row):
        couple_to_index[couple] = i

    for i in range(0, len(row), 2):
        partner = row[i] ^ 1  # Find the partner of the current person
        partner_index = couple_to_index[partner]

        if partner_index != i + 1:
            # If the partner is not sitting next to the current person, swap them
            row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
            couple_to_index[row[partner_index]] = partner_index
            couple_to_index[row[i + 1]] = i + 1
            swaps += 1

    return swaps

# Example usage:
couples_row = [1, 3, 4, 0, 2, 5]
result = min_swaps_to_rearrange_couples(couples_row)
print(result)  # Output: 2
