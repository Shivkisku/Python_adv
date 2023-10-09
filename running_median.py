import heapq

class RunningMedian:
    def __init__(self):
        self.min_heap = []  # Contains the larger half of elements
        self.max_heap = []  # Contains the smaller half of elements

    def insert(self, num):
        # Insert the new element into the appropriate heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance the heaps if needed
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]

def compute_running_median(sequence):
    rm = RunningMedian()
    for num in sequence:
        rm.insert(num)
        print(rm.get_median())

# Example usage:
compute_running_median([2, 1, 5, 7, 2, 0, 5])
