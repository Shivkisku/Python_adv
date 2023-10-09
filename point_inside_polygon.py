def is_point_inside_polygon(polygon, p):
    n = len(polygon)

    if n < 3:
        return False  # Polygon must have at least 3 points

    # Create a point outside the polygon, to be used for the ray
    ray = (float('inf'), p[1])

    intersections = 0

    for i in range(n):
        p1, p2 = polygon[i], polygon[(i + 1) % n]

        if is_point_on_segment(p1, p2, p):
            return False  # The point is on the boundary

        if p1[1] == p2[1]:  # Skip horizontal edges
            continue

        if p[1] < min(p1[1], p2[1]) or p[1] >= max(p1[1], p2[1]):
            continue

        x_intersection = (p[1] - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]

        if x_intersection > p[0]:
            intersections += 1

    return intersections % 2 == 1

def is_point_on_segment(p1, p2, p):
    return (
        min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0]) and
        min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1])
    )

# Example usage:
polygon = [(1, 1), (4, 1), (4, 4), (1, 4)]
point = (2, 2)

result = is_point_inside_polygon(polygon, point)
print(result)  # Output: True
