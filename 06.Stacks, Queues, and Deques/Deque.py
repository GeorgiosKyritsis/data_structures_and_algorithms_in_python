__author__ = 'inamoto21'

from Stack import Empty


class ArrayDeque:
    """Double-ended queue using a list as underlying storage."""
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return self._data.__str__()

    def is_empty(self):
        return len(self._data) == 0

    def add_first(self, e):
        self._data.insert(0, e)

    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        for j in range(len(self._data)-1):
            self._data[j] = self._data[j+1]
        self._data.pop()
        return self._data

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        self._data.pop()
        return self._data

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[0]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._data[-1]


def main():
    s = ArrayDeque()
    print('-------Add first -> 1--------')
    s.add_first(1)
    print('-------Add last -> 10--------')
    s.add_last(10)
    print('-------Add first -> 2--------')
    s.add_first(2)
    print('-------Add last -> 12--------')
    s.add_last(12)
    print('-------Add last -> 100--------')
    s.add_last(100)
    print(s)
    print('-------Print last element--------')
    print(s.last())
    print('-------Delete last element--------')
    print(s.delete_last())
    print('-------Delete first element--------')
    print(s.delete_first())
    print('-------Add last -> 1000--------')
    s.add_last(1000)
    print(s)
    print('-------Add first -> 1000--------')
    s.add_first(1000)
    print(s)


if __name__ == '__main__':
    main()





