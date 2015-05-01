__author__ = 'inamoto21'


class PriorityQueueBase:
    class _Item:
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list"""

    def __init__(self):
        self._data = []

    def add(self, key, value):
        """Add a key value pair"""
        self._data.append(self._Item(key, value))
        self._data.sort()

    def remove(self):
        """Remove the element with the minimum key that is the first element"""
        del self._data[0]

    def min(self):
        """Return but not remove the element with the minimum key that is the first element"""
        return self._data[0]._key, self._data[0]._value             # Return a tuple

    def __iter__(self):
        for c in self._data:
            yield ("key: " + str(c._key), "value: " + str(c._value))

    def __len__(self):
        return self._data.__len__()

    def is_empty(self):
        return len(self) == 0

if __name__ == '__main__':
    s = SortedPriorityQueue()
    s.add(1, 10)
    s.add(2, 20)
    s.add(0, 100)
    s.add(-1, 1000)
    print("-------Printing the elements of the Priority Queue---------")
    for i in s:
        print(i)
    print("-------Removing 2 elements from the Priority Queue---------")
    s.remove()
    s.remove()
    print("-------Printing the element from the Priority Queue with the minimum key---------")
    print(s.min())
    assert len(s) == 2