import tkinter as tk

from tkinter import messagebox

class KikTacToe:
    def __init__(self, window):
        self.window = window
        self.window.title("TicTacToe")

    def create_game(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=('Arial', 50), height=2, width=6, bg="blue",
                                    command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, col=j, sticky="nsew")
    
    def initialize_veriables(self):
        self.board = [[0,0,0], [0,0,0], [0,0,0]]
        self.current_player = 1

    def handle_click(self, row, col):
        pass


