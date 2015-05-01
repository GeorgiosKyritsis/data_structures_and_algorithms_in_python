__author__ = 'inamoto21'

class HeapPriorityQueue:
    """A min-oriented priority queue implemented with a binary heap"""

    class _Item:
        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add(self, key, value):
        """Add a pair key, value to priority queue"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        """Return but not remove (k,v) tuple with the minimum key"""
        if self.is_empty():
            raise IndexError('Empty priority queue')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        self._swap(0, len(self._data) - 1)          # put the minimum at the end
        item = self._data.pop()                     # and remove it from the list
        self._downheap(0)
        return (item._key, item._value)

    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """Swap the elements at indices i and j of array"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left              # although right might be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def __iter__(self):
        for j in range(len(self)):
            node = self._data[j]
            yield (node._key, node._value)          # return a tuple (k, v)

if __name__ == '__main__':
    s = HeapPriorityQueue()
    s.add(1, 10)
    s.add(2,20)
    s.add(3,23)
    s.add(0, 800)
    s.add(-1, 500)
    assert len(s) == 5
    print("------Printing the elements of the Priority Queue------")
    for j in s:
        print(j)
    print("------Deleting the element of the Priority Queue------")
    s.remove_min()
    print("------Printing the elements of the Priority Queue------")
    for j in s:
        print(j)
    assert len(s) == 4