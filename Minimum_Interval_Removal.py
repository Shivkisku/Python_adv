def min_intervals_to_remove(intervals):
    if not intervals:
        return 0

    # Sort intervals by their end points
    intervals.sort(key=lambda x: x[1])

    count = 0
    end = intervals[0][1]

    for interval in intervals[1:]:
        if interval[0] < end:
            # Overlapping interval found, increment count
            count += 1
        else:
            # Non-overlapping interval, update end point
            end = interval[1]

    return count

# Example usage:
intervals = [(7, 9), (2, 4), (5, 8)]
result = min_intervals_to_remove(intervals)
print(result)  # Output: 1
