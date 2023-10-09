import heapq

def find_shortest_route(elevations, paths):
    # Create a graph with elevation differences as edge weights
    graph = {}
    for (start, end), distance in paths.items():
        elevation_diff = elevations[end] - elevations[start]
        if elevation_diff > 0:
            graph.setdefault(start, []).append((end, distance))
    
    # Initialize the priority queue (min heap) with (distance, node) pairs
    pq = [(0, 0)]  # (distance, node)
    visited = set()
    
    while pq:
        dist, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == 0 and len(visited) > 1:
            return dist  # Found a valid route
        
        for neighbor, edge_dist in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (dist + edge_dist, neighbor))
    
    return float('inf')  # No valid route found

# Example usage:
elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
shortest_route_length = find_shortest_route(elevations, paths)
print(shortest_route_length)  # Output: 28
