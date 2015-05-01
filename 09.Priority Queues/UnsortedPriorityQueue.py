__author__ = 'inamoto21'


class PriorityQueueBase:
    class _Item:
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with an unsorted list"""

    def __init__(self):
        self._data = []

    def _find_min(self):            # non public utility function
        """Return the Position (index) of item with minimum key"""

        if self.is_empty():
            raise IndexError("Priority queue is empty")
        small = self._data[0]._key
        index = 0
        index_key = 0
        for e in self._data:
            if e._key < small:
                small = e._key
                index_key = index
            index += 1
        return index_key


    def add(self, key, value):
        """Add a key value pair"""
        self._data.append(self._Item(key, value))

    def remove(self):
        """Remove the element with the minimum key"""
        p = self._find_min()
        print("item with key {} and value {} deleted".format(self._data[p]._key, self._data[p]._value))
        del self._data[p]

    def min(self):
        """Return but not remove the element with the minimum key"""
        p = self._find_min()
        print("item with key {} and value {} has the minimum key".format(self._data[p]._key, self._data[p]._value))
        return (self._data[p]._key, self._data[p]._value)

    def __iter__(self):
        for c in self._data:
            yield ("key: " + str(c._key), "value: " + str(c._value))

    def __len__(self):
        return self._data.__len__()

    def is_empty(self):
        return len(self) == 0

if __name__ == '__main__':
    s = UnsortedPriorityQueue()
    s.add(1, 10)        # add key=1, value=10
    s.add(0, 50)        # add key=0, value=50
    s.add(2, 20)
    s.add(-1, 100)
    s.add(0, 1000)
    assert len(s) == 5
    print("-------Printing the elements of the Priority Queue---------")
    for i in s:
        print(i)
    print("-------Removing the element with the minimum key from the Priority Queue---------")
    s.remove()
    assert len(s) == 4
    print("-------Printing the elements of the Priority Queue---------")
    for i in s:
        print(i)
    print("-------Removing the element with the minimum key from the Priority Queue---------")
    s.remove()
    print("-------Printing the element with the minimum key from the Priority Queue---------")
    s.min()
    assert len(s) == 3
    print("-------Printing the elements of the Priority Queue---------")
    for i in s:
        print(i)