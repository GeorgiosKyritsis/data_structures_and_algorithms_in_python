__author__ = 'inamoto21'

import GameEntry

class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order"""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity.
        All entries are initially None"""

        self._board = [None] * capacity     # list of 10 None elements
        self._n = 0                         # number of actual entries

    def __getitem__(self, k):
        """Return entry at index k"""
        return self._board[k]

    def __str__(self):
        """Return string representation of the high score list"""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Adding entry to high scores."""
        score = entry.get_score()

        # Does the new entry qualify as high score.
        # The high score is True if board not full or score is higher than last entry
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):      # no score drops from list
                self._n += 1                    # overall number increases


            # shift lower scores rightwards to make entry
            j = self._n - 1
            while j > 0 and score > self._board[j-1].get_score():
                self._board[j] = self._board[j-1]           # shift entry from j-1 to j
                j -= 1                                      # decrement j
            self._board[j] = entry                          # well done, add new entry


def main():
    print("---------------Entries----------------------\n")
    george = GameEntry.GameEntry("George", 100)             # From GameEntry module I use the GameEntry class, and create an object
    thanasis = GameEntry.GameEntry("Thanasis", 120)
    john = GameEntry.GameEntry("John", 90)
    vana = GameEntry.GameEntry("Vana", 80)
    print(george)
    print(thanasis)
    print(john)
    print(vana)

    print("\n------------Adding Elements to Leaderboard---------------------\n")
    leader_board = Scoreboard()
    leader_board.add(george)
    print(leader_board)
    print("\n================================\n")
    leader_board.add(thanasis)
    print(leader_board)
    print("\n================================\n")
    leader_board.add(john)
    print(leader_board)
    print("\n================================\n")
    leader_board.add(vana)
    print(leader_board)
    print("\n================================\n")


if __name__ == '__main__':
    main()




