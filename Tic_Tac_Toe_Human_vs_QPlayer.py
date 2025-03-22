import numpy as np
import tkinter as tk
import copy
import pickle as pickle    # cPickle is available in Python 2.x only, otherwise use pickle

from Q_Learning_Tic_Tac_Toe import Game, HumanPlayer, QPlayer

try:
    Q = pickle.load(open("Q_epsilon_09_Nepisodes_200000.p", "rb"))
    print("Q-table loaded successfully.")
except FileNotFoundError:
    print("Error: Q-table file not found. Ensure the training script has been run.")
    exit(1)

root = tk.Tk()

# Customize button styles (if buttons are part of the Game class)
style = {"font": ("Arial", 16), "bg": "white", "fg": "black", "width": 5, "height": 2}
# Pass `style` to the Game class or apply it to buttons in the Game implementation

player1 = HumanPlayer(mark="X")
player2 = QPlayer(mark="O", epsilon=0)

game = Game(root, player1, player2, Q=Q)

game.play()
root.mainloop()
root.destroy()  # Ensure the Tkinter root window is properly closed
