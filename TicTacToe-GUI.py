import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import sys
class TicTacToeGUI:
    def __init__(self):
        self.window = None
        self.size = self.ask_size()
        if self.size:
            self.initialize_window()
            self.player = 'X' if random.randint(0, 1) == 1 else 'O'
            self.create_widgets()
            self.update_turn_label()
            self.window.mainloop()

    def ask_size(self):
        while True:
            size = simpledialog.askinteger("Board Size", "Enter size of the board (3-6):")
            if size is None:
                sys.exit()
            elif 3 <= size <= 6:
                return size
            else:
                messagebox.showerror("Invalid input", "Please enter a valid size between 3 and 6.")

    def initialize_window(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.config(padx=10)
    def create_widgets(self):
        self.turn_label = tk.Label(self.window, text=f"Player {self.player}'s turn", font=('normal', 20))
        self.turn_label.grid(row=0, column=0, columnspan=self.size)

        self.board = [['-' for _ in range(self.size)] for _ in range(self.size)]
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                button = tk.Button(self.window, text=' ', font=('normal', 20), bg='thistle2', width=5, height=2,
                                   command=lambda row=i, col=j: self.fix_spot(row, col))
                button.grid(row=i+1, column=j)
                self.buttons[i][j] = button

        restart_button = tk.Button(self.window, text='Restart', font=('normal', 20), bg='deeppink3', width=10, height=2, command=self.restart)
        restart_button.grid(row=self.size + 1, column=0, columnspan=self.size, pady=10)

    def fix_spot(self, row, col):
        if self.board[row][col] == '-':
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)
            if self.is_player_win(self.player):
                self.display_message(f"Player {self.player} wins!")
            elif self.is_board_filled():
                self.display_message("It's a draw!")
            else:
                self.player = 'X' if self.player == 'O' else 'O'
                self.update_turn_label()

    def is_player_win(self, player):
        for i in range(self.size):
            if all(self.board[i][j] == player for j in range(self.size)) or \
               all(self.board[j][i] == player for j in range(self.size)):
                return True
        if all(self.board[i][i] == player for i in range(self.size)) or \
           all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
            return True
        return False

    def is_board_filled(self):
        return all(item != '-' for row in self.board for item in row)

    def display_message(self, message):
        messagebox.showinfo("Game Over", message)
        self.disable_buttons()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def update_turn_label(self):
        self.turn_label.config(text=f"Player {self.player}'s turn")

    def restart(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.create_widgets()
        self.player = 'X' if self.player=='O' else 'O'
        self.update_turn_label()

tic_tac_toe_gui = TicTacToeGUI()
