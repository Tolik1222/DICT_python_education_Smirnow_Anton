"""Domino game used to simulate a game of dominoes between a player and a computer"""

import random


# Initializes the game object with empty list for stock pieces, player pieces, computer pieces, domino snake, and status


class DominoGame:
    def __init__(self):
        self.stock_pieces = []
        self.player_pieces = []
        self.computer_pieces = []
        self.domino_snake = []
        self.status = ""

    # Starts the game, deals the pieces, determines the starting piece and player, manages player and computer moves

    def start_game(self):
        self.create_domino_set()
        self.distribute_pieces()
        self.determine_starting_piece_and_player()
        while not self.check_game_end():
            self.display_game_state()
            if self.status == "player":
                self.player_make_move()
            else:
                self.computer_make_move()
            self.switch_turn()
        self.display_game_state()
        print(self.end_game_message())

    # Creates a full set of dominoes with 28 pieces

    def create_domino_set(self):
        for i in range(7):
            for j in range(i, 7):
                self.stock_pieces.append([i, j])

    # Deals pieces to the player and computer from the stock

    def distribute_pieces(self):
        random.shuffle(self.stock_pieces)
        self.player_pieces = self.stock_pieces[:7]
        self.computer_pieces = self.stock_pieces[7:14]
        self.stock_pieces = self.stock_pieces[14:]

    # Determines the starting piece and player

    def determine_starting_piece_and_player(self):
        max_double = max([max(piece) for piece in self.stock_pieces])
        for piece in self.stock_pieces:
            if max(piece) == max_double:
                self.domino_snake.append(piece)
                self.stock_pieces.remove(piece)
                self.status = "player"
                break
        else:
            random.shuffle(self.stock_pieces)
            self.player_pieces = self.stock_pieces[:7]
            self.computer_pieces = self.stock_pieces[7:14]
            self.stock_pieces = self.stock_pieces[14:]
            self.status = "computer"

    # Displays the current state of the game, including player and computer pieces, domino snake, and turn status

    def display_game_state(self):
        print("=" * 70)
        print("Stock size:", len(self.stock_pieces))
        print("Computer pieces:", len(self.computer_pieces))
        print(self.domino_snake[0], end="")
        if len(self.domino_snake) > 1:
            print("..." + str(self.domino_snake[-1]), end="")
        print()
        print("Your pieces:")
        for i, piece in enumerate(self.player_pieces, start=1):
            print(f"{i}:{piece}")
        print("Status:", end=" ")
        if self.status == "player":
            print("It's your turn to make a move. Enter your command.")
        else:
            print("Computer is about to make a move. Press Enter to continue...")

    # Returns the end game message

    def end_game_message(self):
        if len(self.player_pieces) == 0:
            return "Status: The game is over. You won!"
        elif len(self.computer_pieces) == 0:
            return "Status: The game is over. The computer won!"
        else:
            return "Status: The game is over. It's a draw!"

    # Manages the player's move

    def player_make_move(self):
        while True:
            try:
                move = int(input("> "))
                if move == 0:
                    if len(self.stock_pieces) > 0:
                        self.player_pieces.append(self.stock_pieces.pop())
                    else:
                        print("No more pieces in stock.")
                elif abs(move) > len(self.player_pieces) or move > len(self.player_pieces):
                    raise ValueError
                elif move < 0:
                    piece = self.player_pieces[move]
                    if piece[0] == self.domino_snake[0][0] or piece[1] == self.domino_snake[0][0]:
                        self.domino_snake.insert(0, piece[::-1])
                        self.player_pieces.pop(move)
                    else:
                        raise ValueError
                else:
                    piece = self.player_pieces[move - 1]
                    if piece[0] == self.domino_snake[-1][1] or piece[1] == self.domino_snake[-1][1]:
                        self.domino_snake.append(piece)
                        self.player_pieces.pop(move - 1)
                    else:
                        raise ValueError
                break
            except (ValueError, IndexError):
                print("Invalid move. Please try again.")

    # Manages the computer's move

    def computer_make_move(self):
        input("Press Enter to allow computer to make a move...")
        max_score = float("-inf")
        best_piece = None
        for piece in self.computer_pieces:
            score = piece[0] + piece[1] + \
                    sum([self.domino_snake.count([i, j]) for i in piece for j in piece])
            if score > max_score:
                max_score = score
                best_piece = piece
        if best_piece:
            if best_piece[0] == self.domino_snake[-1][1]:
                self.domino_snake.append(best_piece)
            elif best_piece[1] == self.domino_snake[-1][1]:
                self.domino_snake.append(best_piece[::-1])
            elif best_piece[1] == self.domino_snake[0][0]:
                self.domino_snake.insert(0, best_piece)
            elif best_piece[0] == self.domino_snake[0][0]:
                self.domino_snake.insert(0, best_piece[::-1])
            self.computer_pieces.remove(best_piece)
        else:
            if len(self.stock_pieces) > 0:
                self.computer_pieces.append(self.stock_pieces.pop())
            else:
                print("Computer skips the move as there are no available pieces.")

    # Switches the turn between player and computer

    def switch_turn(self):
        if self.status == "player":
            self.status = "computer"
        else:
            self.status = "player"

    # Checks if the game has ended

    def check_game_end(self):
        if len(self.player_pieces) == 0 or len(self.computer_pieces) == 0:
            return True
        snake_ends = [self.domino_snake[0][0], self.domino_snake[-1][1]]
        for num in snake_ends:
            if sum(piece.count(num) for piece in self.domino_snake) == 8:
                return True
        return False


# creating the game and start
game = DominoGame()
game.start_game()
