import random

class Game2048:
    def __init__(self):
        self.size = 4
        self.board = [[0] * self.size for _ in range(self.size)]
        self.score = 0
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        empty_tiles = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == 0]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            self.board[r][c] = 2 if random.random() < 0.9 else 4

    def compress(self, row):
        new_row = [i for i in row if i != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row

    def merge(self, row):
        for i in range(self.size - 1):
            if row[i] == row[i + 1] and row[i] != 0:
                row[i] *= 2
                row[i + 1] = 0
                self.score += row[i]
        return row

    def move_left(self):
        new_board = []
        for row in self.board:
            new_row = self.compress(row)
            new_row = self.merge(new_row)
            new_row = self.compress(new_row)
            new_board.append(new_row)
        self.board = new_board

    def rotate_board(self):
        self.board = [list(row) for row in zip(*self.board[::-1])]

    def move(self, direction):
        for _ in range(direction):
            self.rotate_board()
        self.move_left()
        for _ in range((4 - direction) % 4):
            self.rotate_board()
        self.spawn_tile()

    def is_game_over(self):
        for row in self.board:
            if 0 in row:
                return False
        for row in self.board:
            for i in range(self.size - 1):
                if row[i] == row[i + 1]:
                    return False
        for c in range(self.size):
            for r in range(self.size - 1):
                if self.board[r][c] == self.board[r + 1][c]:
                    return False
        return True

    def print_board(self):
        for row in self.board:
            print(row)
        print(f'Score: {self.score}')

if __name__ == "__main__":
    game = Game2048()
    game.print_board()
    while not game.is_game_over():
        move = input("Enter move (w/a/s/d): ")
        if move == 'w':
            game.move(1)
        elif move == 'a':
            game.move(0)
        elif move == 's':
            game.move(3)
        elif move == 'd':
            game.move(2)
        game.print_board()
    print("Game Over")
