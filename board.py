class Board:
    def __init__(self):
        self.game_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def set_items(self, user, position, game_board):
        game_board[position] = user
        return game_board

    @property
    def gameBoard(self):
        return self.game_board

    def clear_board(self):
        self.game_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def place_taken(self, game_board, index):
        if game_board[index] != ' ':
            return True

    def full_board(self, game_board):
        for i in range(1, 10):
            if game_board[i] == ' ':
                return False
        return True

    def game_won(self, game_board):
        win = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for i in win:
            if game_board[i[0]] == game_board[i[1]] == game_board[i[2]] and game_board[i[0]] != ' ':
                return True

    def print_board(self, game_board):
        idx = 0
        for i in range(1, 4):
            for j in range(1, 4):
                idx += 1
                if j != 3:
                    print(game_board[idx], end='')
                    print('|', end='')
                else:
                    print(game_board[idx])