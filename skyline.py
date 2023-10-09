import heapq  # Add this line to import the heapq module

def getSkyline(buildings):
    if not buildings:
        return []

    # Combine the start and end points of buildings and mark start points as negative
    events = [(l, -h, r) for l, r, h in buildings]
    events += [(r, 0, 0) for _, r, _ in buildings]

    # Sort the events based on their x-coordinate (left end or right end)
    events.sort()

    result = []
    max_heap = [(0, float('inf'))]  # Max heap to keep track of heights

    for x, neg_height, r in events:
        while max_heap and x >= max_heap[0][1]:
            heapq.heappop(max_heap)  # Remove heights that have passed

        if neg_height:
            heapq.heappush(max_heap, (neg_height, r))  # Add height to max heap

        # The height at the top of the max heap is the maximum height at this x-coordinate
        if not result or result[-1][1] != -max_heap[0][0]:
            result.append((x, -max_heap[0][0]))

    return result

# Example usage:
if __name__ == "__main__":
    buildings = [(0, 15, 3), (4, 11, 5), (19, 23, 4)]
    result = getSkyline(buildings)
    print(result)  # Output: [(0, 3), (4, 5), (11, 3), (15, 0), (19, 4), (23, 0)]
