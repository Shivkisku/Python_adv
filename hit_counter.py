from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def record(self, timestamp):
        self.hits.append(timestamp)

    def total(self):
        return len(self.hits)

    def range(self, lower, upper):
        count = 0
        for timestamp in self.hits:
            if lower <= timestamp <= upper:
                count += 1
            # Since the hits are in ascending order, we can break once we go beyond 'upper'
            elif timestamp > upper:
                break
        return count

# Example usage:
hit_counter = HitCounter()
hit_counter.record(1)  # Records a hit at timestamp 1
hit_counter.record(2)  # Records a hit at timestamp 2
hit_counter.record(3)  # Records a hit at timestamp 3

total_hits = hit_counter.total()  # Returns the total number of hits (3)
print("Total Hits:", total_hits)

hits_in_range = hit_counter.range(2, 4)  # Returns the number of hits between timestamps 2 and 4 (2)
print("Hits in Range:", hits_in_range)
