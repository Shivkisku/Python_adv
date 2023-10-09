import heapq

def find_median(arr, k):
    if k % 2 == 0:
        # If k is even, we'll maintain two heaps: max_heap for the left half and min_heap for the right half
        max_heap = []  # Max-heap for the left half (contains smaller elements)
        min_heap = []  # Min-heap for the right half (contains larger elements)
        median = None  # Initialize the median

        for i in range(len(arr)):
            if i >= k:
                # Remove the element that's no longer in the window
                element_to_remove = arr[i - k]
                if element_to_remove <= -max_heap[0]:
                    heapq.heappop(max_heap)
                else:
                    heapq.heappop(min_heap)

            # Add the current element to the appropriate heap
            if not max_heap or arr[i] <= -max_heap[0]:
                heapq.heappush(max_heap, -arr[i])
            else:
                heapq.heappush(min_heap, arr[i])

            # Balance the heaps
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            if i >= k - 1:
                # Calculate the median and print it
                if k % 2 == 0:
                    median = (-max_heap[0] + min_heap[0]) / 2
                else:
                    median = -max_heap[0]
                print(median)

    else:
        # If k is odd, we'll maintain a single max_heap
        max_heap = []  # Max-heap for the left half (contains smaller elements)

        for i in range(len(arr)):
            if i >= k:
                # Remove the element that's no longer in the window
                element_to_remove = arr[i - k]
                max_heap.remove(-element_to_remove)
                heapq.heapify(max_heap)

            # Add the current element to the max_heap
            heapq.heappush(max_heap, -arr[i])

            if i >= k - 1:
                # Calculate the median and print it
                median = -max_heap[0]
                print(median)

# Example usage:
arr = [-1, 5, 13, 8, 2, 3, 3, 1]
k = 3
find_median(arr, k)
