def is_crossword_grid(grid):
    def is_word_start(i, j):
        # Check if the cell (i, j) is the start of an "across" or "down" word
        if grid[i][j] == 'B':
            return False
        if i == 0 or grid[i - 1][j] == 'B':
            return True
        if j == 0 or grid[i][j - 1] == 'B':
            return True
        return False

    def is_valid_word_length(i, j, direction):
        # Check if the word in the specified direction is at least three letters long
        if direction == 'across':
            while j < len(grid[i]) and grid[i][j] != 'B':
                j += 1
            return j - start_j >= 3
        elif direction == 'down':
            while i < len(grid) and grid[i][j] != 'B':
                i += 1
            return i - start_i >= 3

    def is_reachable(i1, j1, i2, j2):
        # Check if two white squares are reachable from each other
        return grid[i1][j1] == 'W' and grid[i2][j2] == 'W'

    N = len(grid)

    # Check every white square
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'W':
                if not is_word_start(i, j):
                    return False
                start_i, start_j = i, j

                if not is_valid_word_length(i, j, 'across'):
                    return False
                if not is_valid_word_length(i, j, 'down'):
                    return False

                for i2 in range(N):
                    for j2 in range(N):
                        if i != i2 or j != j2:
                            if not is_reachable(i, j, i2, j2):
                                return False

    # Check rotational symmetry
    for i in range(N):
        for j in range(N):
            if grid[i][j] != grid[N - 1 - i][N - 1 - j]:
                return False

    return True

# Example usage:
grid = [
    ['B', 'W', 'B', 'B', 'B'],
    ['B', 'W', 'W', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B', 'B']
]

result = is_crossword_grid(grid)
print(result)  