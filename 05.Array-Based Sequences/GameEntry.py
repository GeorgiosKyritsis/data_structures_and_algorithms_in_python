__author__ = 'inamoto21'


class GameEntry:
    """Represents one entry of a list of high scores"""

    def __init__(self, name, score):  # Constructor (2 instance variables)
        self._name = name
        self._score = score

    def get_name(self):         # name getter
        return self._name

    def get_score(self):        # score getter
        return self._score

    def __str__(self):
        return '({0}, {1})'.format(self._name, self._score)     # e.g., '(George, 28)'
