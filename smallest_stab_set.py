def find_smallest_stab_set(intervals):
    if not intervals:
        return []

    # Sort intervals by their right endpoint
    intervals.sort(key=lambda x: x[1])

    stab_points = [intervals[0][1]]
    last_stab_point = intervals[0][1]

    for interval in intervals:
        start, end = interval
        if start > last_stab_point:
            stab_points.append(end)
            last_stab_point = end

    return stab_points

# Example usage:
intervals = [(1, 4), (4, 5), (7, 9), (9, 12)]
stab_points = find_smallest_stab_set(intervals)
print(stab_points)  # Output: [4, 9]
