from board import Board


class Game:

    def game_start(self):
        self.controlBoard = Board
        self.game_board = self.controlBoard().gameBoard
        self.player1 = 'O'
        self.player2 = 'X'
        print('Welcome to TicTacToe Game')
        print('Enter player1 name:')
        self.player1 = input(' : ')
        print("Enter player2 name:")
        self.player2 = input(' : ')
        print('Instructions: 1) Each place represented by keys 1-9')
        print('              2) Starting from left column each time and moving along the row')
        self.controlBoard().print_board(self.game_board)
        self.turn = 1

    def game_end(self, result):
        replay = input(f"{result}. Press 0 to quit or 1 to play again: ")
        if replay == '0':
            self.game_running = False
        elif replay == '1':
            self.game_running = True
            self.game_start()
        else:
            print("Invalid input. Please enter 0 to quit or 1 to play again.")
            self.game_end(result)

    def taketurn(self, user, item):
        print(user + " Press a key 1-9")
        try:
            position = int(input(": "))
            if position > 9 or position < 1:
                raise ValueError
        except ValueError:
            print('Pick a number between 1-9')
            return self.taketurn(user, item)

        if self.controlBoard().place_taken(self.game_board, position):
            print("That place is taken")
            return self.taketurn(user, item)
        else:
            self.controlBoard().set_items(item, position, self.game_board)
            self.controlBoard().print_board(self.game_board)
            if self.controlBoard().game_won(self.game_board):
                result = f"{user} wins"
                self.game_end(result)
                return

        if self.controlBoard().full_board(self.game_board):
            result = 'It\'s a draw! You both lose'
            self.game_end(result)
            return

    def main(self):
        self.game_running = True
        self.game_start()
        while self.game_running:
            if self.turn % 2 != 0:
                self.taketurn(self.player1, 'O')
            else:
                self.taketurn(self.player2, 'X')

            self.turn += 1


if __name__ == '__main__':
    Game().main()
