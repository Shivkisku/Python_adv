import math

def find_nearest_k_points(points, central_point, k):
    def distance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Calculate distances from the central point to all other points
    distances = [(point, distance(point, central_point)) for point in points]

    # Sort the distances by distance in ascending order
    distances.sort(key=lambda x: x[1])

    # Select the k nearest points
    nearest_k_points = [point[0] for point in distances[:k]]

    return nearest_k_points

# Example usage:
points = [(0, 0), (5, 4), (3, 1)]
central_point = (1, 2)
k = 2
result = find_nearest_k_points(points, central_point, k)
print(result)  # Output: [(0, 0), (3, 1)]
