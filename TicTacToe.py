import random
class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = []
        self.current_player = None

    def create_board(self):
        self.board = [['-' for _ in range(self.size)] for _ in range(self.size)]

    def get_random_first_player(self):
        return random.choice(['X', 'O'])

    def fix_spot(self, row, col, player):
        if not (0 <= row < self.size) or not (0 <= col < self.size):
            raise ValueError("Invalid spot. Please choose a spot within the range of the board.")
        if self.board[row][col] != '-':
            raise ValueError("Spot is already filled. Please choose another spot.")
        self.board[row][col] = player

    def is_player_win(self, player):
        win_conditions = [
            all(self.board[i][j] == player for j in range(self.size)) for i in range(self.size)
        ] + [
            all(self.board[i][j] == player for i in range(self.size)) for j in range(self.size)
        ] + [
            all(self.board[i][i] == player for i in range(self.size)),
            all(self.board[i][self.size - 1 - i] == player for i in range(self.size))
        ]
        return any(win_conditions)

    def is_board_filled(self):
        return all(item != '-' for row in self.board for item in row)

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            print(" ".join(row))
        print()

    def start(self):
        self.create_board()
        self.current_player = self.get_random_first_player() if self.current_player is None else self.swap_player_turn(self.current_player)
        player = self.current_player
        while True:
            self.show_board()
            print(f"Now is Player {player}'s turn")
            while True:
                try:
                    row, col = map(int, input("Enter row and column numbers (1-based, e.g., 1 3) to fix spot: ").split())
                    self.fix_spot(row - 1, col - 1, player)
                    break
                except ValueError as e:
                    print(e)
            if self.is_player_win(player):
                print(f"\nPlayer {player} wins the game!")
                break
            if self.is_board_filled():
                print("Match Draw!")
                break
            player = self.swap_player_turn(player)
        self.show_board()
        self.prompt_restart()

    def prompt_restart(self):
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        if restart == 'yes':
            self.start()
        else:
            print("Thanks for playing!")

while True:
    try:
        size = int(input("Input size of board (3-10): "))
        if size < 3 or size > 10:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a valid number between 3 and 10.")

tic_tac_toe = TicTacToe(size)
tic_tac_toe.start()
