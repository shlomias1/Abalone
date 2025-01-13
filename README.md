# **Abalone Game Implementation**

This repository contains a Python implementation of the **Abalone Game**, a strategic board game where players compete to push their opponent's pieces off the board.

---

## **Features**
- **Board Representation**: Implements a hexagonal board with an initial setup for the black and white players.
- **Player Mechanics**:
  - Turn-based system for black and white players.
  - Switch players automatically after each turn.
- **Move Validation**:
  - Supports single-disc and multi-disc moves (up to three discs).
  - Validates moves based on the board state and rules of the game.
- **Game Status**:
  - Tracks removed pieces for each player.
  - Determines when a player has won by removing 6 opponent pieces.
- **Cloning**:
  - Allows creating a copy of the current game state.
- **Encoding and Decoding**:
  - Encodes the board state into a numerical representation.
  - Decodes an action index into a move.
- **Interactive Gameplay**:
  - Text-based interface to play the game.

---

## **Usage**
### **Requirements**
- Python 3.8 or higher.

### **Running the Game**
1. Clone the repository or download the script.
2. Run the script using:
   ```bash
   python abalone_game.py
   ```
3. Follow the prompts to play the game:
   - Enter the row and column of the disc you want to move.
   - Choose the number of discs (1-3).
   - Specify the direction (e.g., `up`, `down`, `left`, `right`, `up-left`, `down-right`).

### **Example Gameplay**
1. The game starts with an initial board state displayed.
2. Players take turns selecting and moving pieces based on the legal moves displayed.
3. The game ends when one player removes 6 of the opponent's pieces.

---

## **Game Rules**
1. Players can move 1-3 discs in a straight line.
2. Moves can be blocked if the path is obstructed.
3. Push opponent's discs off the board by forming a stronger line (e.g., 2 vs 1).
4. The game ends when one player removes 6 opponent pieces.

---

## **Code Overview**
### **Classes and Methods**
- **`AbaloneGame`**:
  - `initialize_board()`: Sets up the initial board state.
  - `legal_moves()`: Calculates all legal moves for the current player.
  - `make_move(move)`: Executes a valid move on the board.
  - `unmake_move(move)`: Reverts a move for undo purposes.
  - `status()`: Returns the game's current status (`ongoing`, `black wins`, `white wins`).
  - `switch_player()`: Switches the turn to the next player.
  - `clone()`: Creates a deep copy of the current game state.
  - `encode() / decode(action)`: Encodes and decodes board states and moves.
- **Main Functionality**:
  - Interactive gameplay loop with input validation.
  - Displays the board state after each move.

---

## **Customization**
- **Board Size**: Modify `initialize_board` to create custom board sizes or configurations.
- **Rules**: Adjust the `legal_moves` method for additional or variant rules.

---

## **Example Board State**
```
    W W W W W
   W W W W W W
    . . . W W W .
     . . . . . . .
      . . . . . . .
     . . . . . . .
    . . . B B B .
   B B B B B B B
    B B B B B
```
- `W`: White pieces.
- `B`: Black pieces.
- `.`: Empty cells.

---

## **Contributing**
Contributions are welcome! If you'd like to improve the game or add features:
1. Fork the repository.
2. Create a new branch.
3. Submit a pull request with your changes.

---

## **License**
This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy the game! 🎮
