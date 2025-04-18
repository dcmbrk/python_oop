from enums import Status
import art

class Utils:
    """Provides utility methods"""

    @staticmethod
    def print_board(board):
        """Prints the board"""
        index = 0
        for r in range(3):
            for c in range(3):
                status = board.grids[index].status

                if status == Status.EMPTY:
                    print(f"| {index} |", end=" ")
                elif status == Status.X or status == Status.O:
                    print (f"| {status.value} |", end=" ")
                else:
                    print(f"| ? |", end=" ")
                index += 1
            print('\n')

    @staticmethod
    def clear_screen():
        """Clears the console"""
        print('\n' * 20)

    @staticmethod
    def greet():
        """Displays the game title"""
        print(art.title)
