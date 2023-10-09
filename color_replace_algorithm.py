def flood_fill(image, sr, sc, newColor):
    if not image:
        return image

    rows, cols = len(image), len(image[0])
    originalColor = image[sr][sc]

    if originalColor == newColor:
        return image

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != originalColor:
            return

        image[r][c] = newColor
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return image

# Example usage:
matrix = [
    ['B', 'B', 'W'],
    ['W', 'W', 'W'],
    ['W', 'W', 'W'],
    ['B', 'B', 'B']
]
sr, sc = 2, 2
newColor = 'G'

result = flood_fill(matrix, sr, sc, newColor)
for row in result:
    print(' '.join(row))
