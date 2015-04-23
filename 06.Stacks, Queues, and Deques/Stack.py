__author__ = 'inamoto21'


class Empty(Exception):
    """Error attempting to access an element from an empty container."""


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        return len(self._data)          #number of elements in stack

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return but not remove the element from the Stack."""
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data[-1]           # the last item in the list

    def pop(self):
        """Remove the element from the top of the stack."""
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data.pop()         # remove last item from the list

    def __str__(self):
        return self._data.__str__()


def main():
    seq = ArrayStack()
    print(seq)
    print("Length: ", len(seq))
    print("\n-------------Push 2 elements------------------\n")
    seq.push(3)
    seq.push(4)
    print(seq)
    print("Length: ", len(seq))
    print("\n-------------Pop 1 element from the Stack------------------\n")
    seq.pop()
    print(seq)
    print("Length: ", len(seq))


if __name__ == '__main__':
    main()



