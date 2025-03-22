# Learning Tic Tac Toe

Reinforcement learning of the game of Tic Tac Toe in Python.

## Description

This project implements the classic Tic Tac Toe game using Q-learning, a reinforcement learning algorithm. The goal is to train a computer player to play optimally by learning from 200,000 games played against itself.

## Features

- Play against a trained Q-learning player.
- Option to play against a "T-hand" player, which uses a simpler strategy.
- Simple and intuitive GUI for gameplay.
- Detailed implementation of Q-learning for educational purposes.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd LearningTicTacToe
   ```
3. Ensure you have Python installed along with the required packages:
   ```bash
   pip install numpy
   ```

## Usage

### Playing Against the QPlayer

To play Tic Tac Toe against a computer player trained by playing 200,000 games against itself, run:

```bash
python Tic_Tac_Toe_Human_vs_QPlayer.py
```

This will bring up a GUI where you can play as "X" against the QPlayer, which plays as "O". The QPlayer is highly skilled and difficult to beat!

## Background

The implementation of Q-learning follows the pseudo-code provided by Meeden [CS63 Lab 6]. Q-learning is a reinforcement learning algorithm that seeks to find the optimal policy for maximizing rewards in a given environment. In this project:

- **State (s):** The marks on the board and the current player's turn.
- **Action (a):** The empty squares on the board.
- **Reward (r):** Positive for player "X" (1.0 for a win, -1.0 for a loss, 0.5 for a tie).

The QPlayer uses an "\(\epsilon\)-greedy" policy during training, where it explores random moves with probability \(\epsilon\) and exploits the learned policy otherwise. After training, \(\epsilon\) is set to 0 for optimal performance.

### Bellman's Equation

The Q-value for a state-action pair is updated using Bellman's equation:
\[
Q(s,a) = r(s,a) + \gamma \max\_{a'} Q(s',a')
\]
where \(s'\) is the next state, \(r(s,a)\) is the reward, and \(\gamma\) is the discount factor (set to 0.9 in this implementation).

### Training

The QPlayer is trained by playing 200,000 games against itself with \(\epsilon = 0.9\). The resulting Q-table is saved and used for gameplay.

## Discussion

After training, the QPlayer is practically unbeatable by a human player. It would be interesting to test its performance against a minimax algorithm or analyze its win/draw rates against the "T-hand" player.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
