import heapq

def k_way_merge_sort(arr, k):
    def merge(arrays):
        heap = [(array[0], i, 0) for i, array in enumerate(arrays) if array]
        heapq.heapify(heap)
        result = []
        
        while heap:
            val, array_idx, elem_idx = heapq.heappop(heap)
            result.append(val)
            if elem_idx + 1 < len(arrays[array_idx]):
                next_val = arrays[array_idx][elem_idx + 1]
                heapq.heappush(heap, (next_val, array_idx, elem_idx + 1))
        
        return result

    if k <= 1:
        return sorted(arr)
    
    n = len(arr)
    chunk_size = (n + k - 1) // k  # Calculate the size of each chunk
    chunks = [arr[i:i + chunk_size] for i in range(0, n, chunk_size)]
    
    sorted_chunks = [sorted(chunk) for chunk in chunks]
    sorted_arr = merge(sorted_chunks)
    
    return sorted_arr

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6]
k = 3
result = k_way_merge_sort(arr, k)
print(result)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]
