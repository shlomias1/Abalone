class AbaloneGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = "black"
        self.opponent = "white"
        self.black_removed = 0
        self.white_removed = 0

    def initialize_board(self):
        board = [["Outside", "Outside", "Outside", "Outside", 'white', 'white', 'white', 'white', 'white'],  # 5
                 ["Outside", "Outside", "Outside", 'white', 'white', 'white', 'white', 'white', 'white'],  # 6
                 ["Outside", "Empty", "Empty", "Empty", 'white', 'white', 'white', "Empty", "Outside"],  # 7
                 ["Outside", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],  # 8
                 ["Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],  # 9
                 ["Outside", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"],  # 8
                 ["Outside", "Empty", "Empty", "Empty", 'black', 'black', 'black', "Empty", "Outside"],  # 7
                 ["Outside", "Outside", "Outside", 'black', 'black', 'black', 'black', 'black', 'black'],  # 6
                 ["Outside", "Outside", "Outside", "Outside", 'black', 'black', 'black', 'black', 'black']]  # 5
        return board

    def __str__(self):
        display = ""
        padding = [4, 3, 2, 1, 0, 1, 2, 3, 4]
        for i, row in enumerate(self.board):
            line = " " * padding[i]
            for cell in row:
                if cell == "Empty":
                    line += ". "
                elif cell == "black":
                    line += "B "
                elif cell == "white":
                    line += "W "
                elif cell == "Outside":
                    line += "  "  # Outside cells are just blank spaces
            display += f"{i} {line.rstrip()}\n"
        return display

    def legal_moves(self):
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1)]
        print("Calculating legal moves...")
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == self.current_player:
                    for di, dj in directions:
                        # Single-disc move
                        ni, nj = i + di, j + dj
                        if self.is_within_board(ni, nj):
                            if self.board[ni][nj] == "Empty":
                                moves.append(((i, j), (ni, nj)))

                        # Multi-disc moves (2 or 3 discs)
                        for num_discs in range(2, 4):
                            group = [(i + k * di, j + k * dj) for k in range(num_discs)]
                            if all(self.is_within_board(x, y) and self.board[x][y] == self.current_player for x, y in group):
                                ni, nj = group[-1][0] + di, group[-1][1] + dj
                                if self.is_within_board(ni, nj) and self.board[ni][nj] == "Empty":
                                    moves.append((group, (ni, nj)))
        return moves

    def is_within_board(self, i, j):
        if 0 <= i < len(self.board) and 0 <= j < len(self.board[i]):
            if self.board[i][j] != "Outside":
                return True
        return False

    def make_move(self, move):
        if isinstance(move[0], list):  # Multi-disc move
            group, (ei, ej) = move
            di = ei - group[-1][0]
            dj = ej - group[-1][1]
            for si, sj in reversed(group):
                self.board[si + di][sj + dj] = self.board[si][sj]
                self.board[si][sj] = "Empty"
        else:  # Single-disc move
            start, end = move
            si, sj = start
            ei, ej = end
            self.board[ei][ej] = self.board[si][sj]
            self.board[si][sj] = "Empty"

        if self.is_edge(ei, ej):
            if self.board[ei][ej] == "black":
                self.black_removed += 1
            else:
                self.white_removed += 1

    def unmake_move(self, move):
        if isinstance(move[0], list):  # Multi-disc move
            group, (ei, ej) = move
            di = group[-1][0] - ei
            dj = group[-1][1] - ej
            for si, sj in group:
                self.board[si][sj] = self.board[si + di][sj + dj]
                self.board[si + di][sj + dj] = "Empty"
        else:  # Single-disc move
            start, end = move
            si, sj = start
            ei, ej = end
            self.board[si][sj] = self.board[ei][ej]
            self.board[ei][ej] = "Empty"

    def clone(self):
        clone_game = AbaloneGame()
        clone_game.board = [row[:] for row in self.board]
        clone_game.current_player = self.current_player
        clone_game.opponent = self.opponent
        clone_game.black_removed = self.black_removed
        clone_game.white_removed = self.white_removed
        return clone_game

    def switch_player(self):
        self.current_player, self.opponent = self.opponent, self.current_player

    def status(self):
        if self.black_removed >= 6:
            return "white wins"
        if self.white_removed >= 6:
            return "black wins"
        return "ongoing"

    def encode(self):
        encoding = []
        for row in self.board:
            for cell in row:
                if cell == "black":
                    encoding.append(1)
                elif cell == "white":
                    encoding.append(-1)
                elif cell == "Empty":
                    encoding.append(0)
        return encoding

    def decode(self, action):
        # Decode an action index into a move
        start, end = action
        si, sj = start
        ei, ej = end
        return ((si, sj), (ei, ej))

    def is_edge(self, i, j):
        return i == 0 or i == len(self.board) - 1 or j == 0 or j == len(self.board[i]) - 1

def main():
    game = AbaloneGame()
    print("Initial board state:")
    print(game)

    while True:
        print("Current player:", game.current_player)
        try:
            print("Legal moves:", game.legal_moves())  # Print all legal moves
            row = int(input("Enter row index: "))
            col = int(input("Enter column index: "))
            num_discs = int(input("Enter number of discs to move (1-3): "))
            direction = input("Enter direction (e.g., 'up', 'down', 'left', 'right', 'up-left', 'down-right'): ")

            directions_map = {
                "up": (-1, 0),
                "down": (1, 0),
                "left": (0, -1),
                "right": (0, 1),
                "up-left": (-1, -1),
                "down-right": (1, 1)
            }

            if direction not in directions_map:
                print("Invalid direction. Try again.")
                continue

            di, dj = directions_map[direction]
            start = (row, col)
            group = [(row + k * di, col + k * dj) for k in range(num_discs)]
            end = (group[-1][0] + di, group[-1][1] + dj)

            if num_discs == 1:
                move = (start, end)
            else:
                move = (group, end)

            legal_moves = game.legal_moves()
            if move in legal_moves:
                game.make_move(move)
                print("Move made:", move)
                print(game)
                if game.status() != "ongoing":
                    print("Game over:", game.status())
                    break
                game.switch_player()
            else:
                print("Illegal move. Legal moves are:", legal_moves)
        except ValueError:
            print("Invalid input. Please enter numbers for row, column, and number of discs.")

if __name__ == "__main__":
    main()
