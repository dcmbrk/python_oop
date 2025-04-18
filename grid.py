from enums import Status, Mark


class Grid:
    """Initializes a grid with index and sets default status to EMPTY"""

    def __init__(self, grid_index):
        self.grid_index = grid_index
        self.status = Status.EMPTY