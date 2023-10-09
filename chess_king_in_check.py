def is_king_in_check(chess_board):
    king_position = None

    # Find the position of the black king (K)
    for i in range(8):
        for j in range(8):
            if chess_board[i][j] == 'K':
                king_position = (i, j)
                break

    if king_position is None:
        return False  # Black king not found

    # Check for threats from white pieces (P, R, N, B, Q)
    threats = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]

    for dx, dy in threats:
        x, y = king_position[0] + dx, king_position[1] + dy
        while 0 <= x < 8 and 0 <= y < 8:
            piece = chess_board[x][y]
            if piece == 'P' or piece == 'R' or piece == 'N' or piece == 'B' or piece == 'Q':
                return True  # King is in check
            elif piece != '.':
                break
            x, y = x + dx, y + dy

    return False  # King is not in check

# Example usage:
chess_board = [
    "...K....",
    "........",
    ".B......",
    "......P.",
    ".......R",
    "..N.....",
    "........",
    ".....Q..",
]

result = is_king_in_check(chess_board)
print(result)  # Output: True
