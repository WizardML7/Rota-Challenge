class RotaGame:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player_pieces = {'X': 3, 'O': 3}
        self.player_turn = 'X'

    def print_board(self):
        for i, row in enumerate(self.board, start=1):
            print('|'.join([' ' if cell == ' ' else str(cell) for cell in row]))
            if i < 3:
                print('-' * 5)

    def is_valid_placement(self, row, col):
        return 1 <= row <= 3 and 1 <= col <= 3 and self.board[row - 1][col - 1] == ' '

    def place_piece(self, row, col):
        if self.is_valid_placement(row, col) and self.player_pieces[self.player_turn] > 0:
            self.board[row - 1][col - 1] = self.player_turn
            self.player_pieces[self.player_turn] -= 1
            return True
        else:
            print("Invalid placement. Try again.")
            return False

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        corner_middle_positions = [(1, 1),  (1, 3),  (2, 2),  (3, 1),  (3, 3)]

        if (
            1 <= start_row <= 3 and 1 <= start_col <= 3 and
            1 <= end_row <= 3 and 1 <= end_col <= 3 and
            self.board[start_row - 1][start_col - 1] == self.player_turn and
            self.board[end_row - 1][end_col - 1] == ' '
        ):
            if (start_row, start_col) in corner_middle_positions:
                # Can move horizontally, vertically, or diagonally by one space
                return (
                    # abs(start_row - end_row) == 1 or abs(start_col - end_col) == 1 or
                    # (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 1)
                    (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 0 or  # Horizontal move
                    abs(start_row - end_row) == 0 and abs(start_col - end_col) == 1 or  # Vertical move
                    abs(start_row - end_row) == 1 and abs(start_col - end_col) == 1)    # Diagonal move
                )
            else:
                # Can only move horizontally or vertically by one space
                return (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 0) or \
                       (abs(start_row - end_row) == 0 and abs(start_col - end_col) == 1)
        else:
            return False

    def make_move(self, start_row, start_col, end_row, end_col):
        if self.is_valid_move(start_row, start_col, end_row, end_col):
            self.board[start_row - 1][start_col - 1], self.board[end_row - 1][end_col - 1] = (
                self.board[end_row - 1][end_col - 1], self.board[start_row - 1][start_col - 1]
            )
            return True
        else:
            print("Invalid move. Try again.")
            return False

    def switch_player_turn(self):
        self.player_turn = 'O' if self.player_turn == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None


def get_player_placement():
    try:
        row = int(input("Enter the row (1, 2, or 3) to place your piece: "))
        col = int(input("Enter the column (1, 2, or 3) to place your piece: "))
        return row, col
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return get_player_placement()

def get_player_move():
    try:
        start_row = int(input("Enter the starting row (1, 2, or 3) to move your piece: "))
        start_col = int(input("Enter the starting column (1, 2, or 3) to move your piece: "))
        end_row = int(input("Enter the ending row (1, 2, or 3) to move your piece: "))
        end_col = int(input("Enter the ending column (1, 2, or 3) to move your piece: "))
        return start_row, start_col, end_row, end_col
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return get_player_move()

def main():
    game = RotaGame()

    # Placement phase
    while sum(game.player_pieces.values()) > 0:
        game.print_board()
        print(f"Player {game.player_turn}, you have {game.player_pieces[game.player_turn]} pieces left.")
        placement_row, placement_col = get_player_placement()
        if game.place_piece(placement_row, placement_col):
            game.switch_player_turn()

    # Movement phase
    while True:
        game.print_board()
        print(f"Player {game.player_turn}, it's your turn to move.")
        start_row, start_col, end_row, end_col = get_player_move()
        
        if game.make_move(start_row, start_col, end_row, end_col):
            winner = game.check_winner()
            if winner:
                game.print_board()
                print(f'Player {winner} wins!')
                break
            else:
                game.switch_player_turn()

if __name__ == "__main__":
    main()
