def find_largest_subset(jobs):
    # Sort the jobs by their end times
    sorted_jobs = sorted(jobs, key=lambda x: x[1])
    
    largest_subset = []
    current_end_time = float('-inf')
    
    for job in sorted_jobs:
        start_time, end_time = job
        if start_time >= current_end_time:
            largest_subset.append(job)
            current_end_time = end_time
    
    return largest_subset

# Example usage:
jobs = [(0, 6), (1, 4), (3, 5), (3, 8), (4, 7), (5, 9), (6, 10), (8, 11)]
largest_subset = find_largest_subset(jobs)
print(largest_subset)
