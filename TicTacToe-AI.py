import tkinter as tk
class TicTacToeAI:
    def __init__(self):
        self.size = 3
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.board = [['-' for _ in range(self.size)] for _ in range(self.size)]
        self.player = 'X'
        self.create_buttons()

    def create_buttons(self):
        for i in range(self.size):
            for j in range(self.size):
                button = tk.Button(self.window, text=' ', font=('normal', 20), bg='mediumorchid1', width=5, height=2,
                                   command=lambda row=i, col=j: self.human_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def restart_game(self):
        self.board = [['-' for _ in range(self.size)] for _ in range(self.size)]
        self.player = 'X'
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j].config(text=' ', state=tk.NORMAL)
        if hasattr(self, 'message_label'):
            self.message_label.destroy()
        if hasattr(self, 'restart_button'):
            self.restart_button.grid_remove()
    def human_move(self, row, col):
        if self.board[row][col] == '-':
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)
            if self.check_win(self.player):
                self.display_winner(self.player)
            elif self.is_board_filled():
                self.display_draw()
            else:
                self.player = 'O'
                self.ai_move()

    def ai_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == '-':
                    self.board[i][j] = self.player
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = '-'
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        self.board[best_move[0]][best_move[1]] = self.player
        self.buttons[best_move[0]][best_move[1]].config(text=self.player)
        if self.check_win(self.player):
            self.display_winner(self.player)
        elif self.is_board_filled():
            self.display_draw()
        else:
            self.player = 'X'

    def minimax(self, board, depth, is_maximizing):
        if self.check_win('O'):
            return 1
        elif self.check_win('X'):
            return -1
        elif self.is_board_filled():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == '-':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = '-'
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(self.size):
                for j in range(self.size):
                    if board[i][j] == '-':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = '-'
                        best_score = min(score, best_score)
            return best_score

    def check_win(self, player):
        for i in range(self.size):
            if all(self.board[i][j] == player for j in range(self.size)) or \
                    all(self.board[j][i] == player for j in range(self.size)):
                return True
        if all(self.board[i][i] == player for i in range(self.size)) or \
                all(self.board[i][self.size - i - 1] == player for i in range(self.size)):
            return True
        return False

    def is_board_filled(self):
        return all(item != '-' for row in self.board for item in row)

    def display_winner(self, player):
        if player == 'O':
            result = "AI wins!"
        else:
            result = "You win!"
        self.message_label = tk.Label(self.window, text=result, font=('normal', 20))
        self.message_label.grid(row=self.size, column=0, columnspan=self.size, pady=5)
        self.disable_buttons()
        self.add_restart_button()

    def display_draw(self):
        self.message_label = tk.Label(self.window, text="It's a draw!", font=('normal', 20))
        self.message_label.grid(row=self.size, column=0, columnspan=self.size, pady=5)
        self.add_restart_button()

    def add_restart_button(self):
        self.restart_button = tk.Button(self.window, text="Restart", font=('normal', 20), bg='palevioletred1',
                                        command=self.restart_game)
        self.restart_button.grid(row=self.size + 1, column=0, columnspan=self.size, pady=10)
    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)
    def start(self):
        self.window.mainloop()


tic_tac_toe_ai = TicTacToeAI()
tic_tac_toe_ai.start()
