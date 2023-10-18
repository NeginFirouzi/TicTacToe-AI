import random
class TicTacToe:

    def __init__(self, size):
        self.size = size
        self.board = []

    def create_board(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append('-')
            self.board.append(row)
    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            raise ValueError("Invalid spot. Please choose a spot within the range of the board.")
        if self.board[row][col] != '-':
            raise ValueError("Spot is already filled. Please choose another spot.")
        else:
            self.board[row][col] = player

    # def is_player_win(self, player):
    #     win = None
    #
    #     n = len(self.board)
    #
    #     for i in range(n):
    #         win = True
    #         for j in range(n):
    #             if self.board[i][j] != player:
    #                 win = False
    #                 break
    #         if win:
    #             return win
    #
    #     for i in range(n):
    #         win = True
    #         for j in range(n):
    #             if self.board[j][i] != player:
    #                 win = False
    #                 break
    #         if win:
    #             return win
    #
    #     # checking diagonals
    #     win = True
    #     for i in range(n):
    #         if self.board[i][i] != player:
    #             win = False
    #             break
    #     if win:
    #         return win
    #
    #     win = True
    #     for i in range(n):
    #         if self.board[i][n - 1 - i] != player:
    #             win = False
    #             break
    #     if win:
    #         return win
    #     return False

    def is_player_win(self, player):
        # Check rows
        for i in range(self.size):
            if all(self.board[i][j] == player for j in range(self.size)):
                return True

        # Check columns
        for j in range(self.size):
            if all(self.board[i][j] == player for i in range(self.size)):
                return True

        # Check primary diagonal
        if all(self.board[i][i] == player for i in range(self.size)):
            return True

        # Check secondary diagonal
        if all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
            return True

        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            self.show_board()
            print(f"Now is Player {player}'s turn")

            while True:
                try:
                    row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
                    try:
                        self.fix_spot(row - 1, col - 1, player)
                        break
                    except ValueError as e:
                        print(e)
                except ValueError:
                    print("Invalid input. Please enter two numbers separated by a space.")


            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            if self.is_board_filled():
                print("Match Draw!")
                break

            player = self.swap_player_turn(player)

        print()
        self.show_board()

while True:
    try:
        size = int(input("Input size of board:"))
        if size < 1:
            raise ValueError("Size must be a positive integer.")
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

tic_tac_toe = TicTacToe(size)
tic_tac_toe.start()
