import numpy as np
import tkinter as tk
import copy
import pickle
from Q_Learning_Tic_Tac_Toe import Game, QPlayer     # Classes used for Tic Tac Toe

root = tk.Tk()
root.title("Tic Tac Toe Training")  # Set window title
root.geometry("400x400")  # Resize the window
root.configure(bg="lightblue")  # Set background color

epsilon = 0.9
player1 = QPlayer(mark="X",epsilon = epsilon)
player2 = QPlayer(mark="O",epsilon = epsilon)
game = Game(root, player1, player2)

N_episodes = 200000
for episodes in range(N_episodes):
    if episodes % 10000 == 0:  # Log progress every 10,000 episodes
        print(f"Training progress: {episodes}/{N_episodes} episodes completed.")
    game.play()
    game.reset()

Q = game.Q

filename = "Q_epsilon_09_Nepisodes_{}.p".format(N_episodes)
pickle.dump(Q, open(filename, "wb"))

print("Training completed. Q-table saved to", filename)
root.destroy()  # Ensure the Tkinter root window is properly closed
