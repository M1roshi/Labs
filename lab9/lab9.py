import tkinter as tk
from tkinter import messagebox, simpledialog
import copy

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики")

        self.board = [None] * 9  # 3x3 поле
        self.buttons = []
        self.player_symbol = None
        self.computer_symbol = None
        self.current_turn = None

        # Создание игрового поля
        self.create_board()

        # Кнопка сброса игры
        self.reset_button = tk.Button(root, text='Сбросить игру', command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def create_board(self):
        """Создание игрового поля."""
        for i in range(9):
            button = tk.Button(self.root, text='', width=10, height=3,
                               font=('Helvetica', 20),
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def choose_symbol(self):
        """Диалог выбора символа игрока."""
        symbol = None
        while symbol not in ['X', 'O']:
            symbol = simpledialog.askstring("Выбор символа", "Выберите символ (X или O):")
            if symbol is None:
                # Если пользователь закрывает диалог, завершить игру
                self.root.destroy()
                exit()
            symbol = symbol.upper()
        self.player_symbol = symbol
        self.computer_symbol = 'O' if symbol == 'X' else 'X'
        self.current_turn = self.player_symbol  # Игрок всегда ходит первым
        messagebox.showinfo("Выбор символа", f"Вы выбрали {self.player_symbol}. Компьютер играет за {self.computer_symbol}.")

    def make_move(self, index):
        """Обработка хода игрока и компьютера."""
        if self.board[index] is None and self.current_turn == self.player_symbol:
            self.board[index] = self.player_symbol
            self.buttons[index].config(text=self.player_symbol, state='disabled')
            if self.check_winner(self.player_symbol):
                messagebox.showinfo("Победа", "Вы победили!")
                self.reset_game()
                return
            elif None not in self.board:
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_game()
                return
            self.current_turn = self.computer_symbol
            self.computer_move()

    def computer_move(self):
        """Ход компьютера с использованием алгоритма Minimax."""
        index = self.get_computer_move()
        if index is not None:
            self.board[index] = self.computer_symbol
            self.buttons[index].config(text=self.computer_symbol, state='disabled')
            if self.check_winner(self.computer_symbol):
                messagebox.showinfo("Победа", "Компьютер победил!")
                self.reset_game()
                return
            elif None not in self.board:
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_game()
                return
            self.current_turn = self.player_symbol

    def check_winner(self, symbol):
        """Проверка победителя."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтали
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
            [0, 4, 8], [2, 4, 6]              # Диагонали
        ]
        for condition in win_conditions:
            if all(self.board[i] == symbol for i in condition):
                return True
        return False

    def reset_game(self):
        """Сброс игры."""
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text='', state='normal')

        # Снова запрашиваем выбор символа
        self.choose_symbol()

        # Игрок всегда ходит первым
        self.current_turn = self.player_symbol
        # Если компьютер ходит первым, сделать ход
        if self.current_turn == self.computer_symbol:
            self.computer_move()

    def get_computer_move(self):
        """Определение лучшего хода для компьютера."""
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] is None:
                self.board[i] = self.computer_symbol
                score = self.minimax(self.board, 0, False)
                self.board[i] = None
                if score > best_score:
                    best_score = score
                    best_move = i
        return best_move

    def minimax(self, board, depth, is_maximizing):
        """Алгоритм Minimax для поиска оптимального хода."""
        if self.check_winner(self.computer_symbol):
            return 1
        elif self.check_winner(self.player_symbol):
            return -1
        elif None not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] is None:
                    board[i] = self.computer_symbol
                    score = self.minimax(board, depth + 1, False)
                    board[i] = None
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] is None:
                    board[i] = self.player_symbol
                    score = self.minimax(board, depth + 1, True)
                    board[i] = None
                    best_score = min(score, best_score)
            return best_score

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    game.choose_symbol()  # Первый выбор знака
    root.mainloop()
