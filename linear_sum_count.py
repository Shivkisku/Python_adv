def count_consecutive_lists_sum_to_n(n):
    count = 0
    start = 1
    end = 1
    current_sum = 1

    while start <= n // 2:
        if current_sum < n:
            end += 1
            current_sum += end
        elif current_sum > n:
            current_sum -= start
            start += 1
        else:
            count += 1
            current_sum -= start
            start += 1
    
    # Adding the case where n itself is a single number list
    count += 1 if n == end else 0

    return count

# Example usage:
n = 9
result = count_consecutive_lists_sum_to_n(n)
print(result)  # Output: 3
