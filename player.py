class Player:
    """Represents a player with a mark (X/O) and record moves."""
    def __init__(self, mark):
        self.mark = mark
        self.grid_data = []

    def record_move(self, x, y):
        """Records the player's move"""
        self.grid_data.append((x, y))

    def __str__(self):
        """Returns player as string"""
        return f"Player {self.mark.value}"