from grid import Grid
from enums import Status, Mark

class Board:
    """Manages the board and logic."""
    def __init__(self):
        self.grids = []
        self.create_table()

    def create_table(self):
        """Initializes an empty 3x3 board/grids"""
        index = 0
        for r in range(3):
            for c in range(3):
                self.grids.append( Grid(index) )
                index += 1

    def is_valid_place(self, index):
        """Checks if a grid  is empty"""
        return self.grids[index].status == Status.EMPTY

    def place_a_mark(self, current_player, index):
        """Places a current player's mark on the board by index input"""
        self.grids[index].status = (
            Status.X if current_player.mark is Mark.X else Status.O
        )

    def has_winner(self, current_player):
        """Checks if the current player has won"""
        current_player_status = Status.X if current_player.mark is Mark.X else Status.O

        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6],
        ]

        for combo in winning_combos:
            count = 0
            for i in combo:
                if self.grids[i].status == current_player_status:
                    count += 1
            if count == 3:
                return True

        return False


    def has_empty_place(self):
        """Checks if the still have empty grid"""
        is_all_placed = True
        for grid in self.grids:
            if grid.status == Status.EMPTY:
                is_all_placed = False
        return is_all_placed