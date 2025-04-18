from board import Board
from player import Player
from enums import Mark
from utils import Utils

class Game:
    """Manages the game flow"""
    def __init__(self):
        """Initializes the game"""
        self.board = Board()
        self.player_x = Player(Mark.X)
        self.player_o = Player(Mark.O)
        self.current_player = self.player_x

    def switch_turn(self):
        """Switches player turn"""
        self.current_player = (
            self.player_o if self.current_player is self.player_x else self.player_x
        )

    def announce_winner(self):
        """Prints the winner"""
        Utils.print_board(self.board)
        print(f"{self.current_player} is winner")

    def announce_draw(self):
        """Prints draw game"""
        Utils.print_board(self.board)
        print("draw")

    def run(self):
        """Starts game with loop"""
        Utils.greet()
        while True:
            Utils.print_board(self.board)

            while True:
                try:
                    move = int(input(f"Player {self.current_player.mark.value}, enter a number (0-8): "))
                    if 0 <= move <= 8 and self.board.is_valid_place(move):
                        break
                    else:
                        print("Invalid move. Please enter a number between 0 and 8, and choose an empty cell.")
                except ValueError:
                    print("Invalid input. Please enter an integer between 0 and 8.")

            self.board.place_a_mark(self.current_player, move)

            if self.board.has_winner(self.current_player):
                self.announce_winner()
                break

            if self.board.has_empty_place():
                self.announce_draw()
                break
            self.switch_turn()
            Utils.clear_screen()

