import heapq

def lowest_cost_pipes(pipes):
    if not pipes:
        return 0

    # Create a set to keep track of visited nodes
    visited = set()

    # Initialize the minimum spanning tree (MST) and the total cost
    mst = []
    total_cost = 0

    # Start from the 'plant' node
    start_node = 'plant'
    visited.add(start_node)

    # Initialize the heap with edges from the 'plant' node
    heap = [(cost, node, start_node) for node, cost in pipes[start_node].items()]
    heapq.heapify(heap)

    while heap:
        cost, node, parent = heapq.heappop(heap)

        if node not in visited:
            mst.append((parent, node))
            total_cost += cost
            visited.add(node)

            # Add edges from the newly added node to the heap
            for neighbor, neighbor_cost in pipes[node].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_cost, neighbor, node))

    return total_cost

# Example usage:
pipes = {
    'plant': {'A': 1, 'B': 5, 'C': 20},
    'A': {'C': 15},
    'B': {'C': 10},
    'C': {}
}
result = lowest_cost_pipes(pipes)
print(result)  # Output: 16
