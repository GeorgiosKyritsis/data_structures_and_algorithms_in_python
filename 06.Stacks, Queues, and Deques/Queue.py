__author__ = 'inamoto21'

from Stack import Empty


class ArrayQueue:
    """FIFO queue using a list as an underlying storage"""

    def __init__(self):
        self._data = []         #create an empty queue

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        """Return but not remove the first element of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self._data[0]            # return the first element of the list

    def dequeue(self):
        """Return and remove the first element of the queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        for j in range(len(self._data)-1):
            self._data[j] = self._data[j+1]
        self._data.pop()
        return self._data

    def enqueue(self, e):
        self._data.append(e)

    def __str__(self):
        return self._data.__str__()


def main():
    s = ArrayQueue()
    print('\n------------Add elements to Queue (Enqueue)')
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    print(s)
    print('\n------------Delete element from Queue (Dequeue)---------------')
    s.dequeue()
    print(s)
    print('\n------------Delete element from Queue (Dequeue)---------------')
    s.dequeue()
    print(s)
    print('\n------------Delete element from Queue (Dequeue)---------------')
    s.dequeue()
    print(s)

if __name__ == '__main__':
    main()

