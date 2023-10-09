class Connect4:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'R'
        self.winner = None

    def display_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 13)

    def drop_disc(self, column):
        if self.winner or ' ' not in self.board[0]:
            return False  # Game is over or column is full

        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                return True

    def check_winner(self):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for row in range(6):
            for col in range(7):
                if self.board[row][col] == ' ':
                    continue

                for dr, dc in directions:
                    r, c = row, col
                    count = 0
                    while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.current_player:
                        r += dr
                        c += dc
                        count += 1

                    if count >= 4:
                        self.winner = self.current_player
                        return True

        return False

    def switch_player(self):
        self.current_player = 'B' if self.current_player == 'R' else 'R'

    def play_game(self):
        while not self.winner and ' ' in self.board[0]:
            self.display_board()
            try:
                column = int(input(f"Player {self.current_player}, enter column (0-6): "))
                if 0 <= column <= 6 and self.drop_disc(column):
                    if self.check_winner():
                        self.display_board()
                        print(f"Player {self.current_player} wins!")
                    else:
                        self.switch_player()
                else:
                    print("Invalid move. Please choose a valid column.")
            except ValueError:
                print("Invalid input. Please enter a number (0-6).")

if __name__ == "__main__":
    game = Connect4()
    game.play_game()
