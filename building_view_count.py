def count_buildings_with_view(heights):
    count = 0
    max_height = 0

    for height in heights:
        if height > max_height:
            count += 1
            max_height = height

    return count

# Example usage:
heights = [3, 7, 8, 3, 6, 1]
result = count_buildings_with_view(heights)
print(result)  # Output: 3
