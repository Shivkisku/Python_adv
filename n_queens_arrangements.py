def is_safe(board, row, col, N):
    # Check if it's safe to place a queen at board[row][col]
    
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N):
    if col >= N:
        return 1  # All queens have been placed successfully

    total_arrangements = 0

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place a queen at (i, col)
            total_arrangements += solve_n_queens_util(board, col + 1, N)
            board[i][col] = 0  # Backtrack

    return total_arrangements

def n_queens(N):
    # Initialize an empty N x N board
    board = [[0] * N for _ in range(N)]

    return solve_n_queens_util(board, 0, N)

# Example usage:
N = 4
arrangements = n_queens(N)
print(f"Number of possible arrangements for {N}-Queens: {arrangements}")
