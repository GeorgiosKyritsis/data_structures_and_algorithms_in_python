__author__ = 'inamoto21'


class LinkedStack:
    """LIFO Stack implementation using a singly linked list as storage"""

    class _Node:
        """Singly linked Node"""
        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def push(self, e):
        """Add element to the top of the stack"""
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        """Return but not remove the element at the top of the list"""
        if self.is_empty():
            return IndexError('Out of bounds')
        node = self._head
        return node._element

    def pop(self):
        """Return and remove the element from the top of the stack"""
        if self.is_empty():
            return IndexError('Out of bounds')
        node = self._head
        answer = node._element
        self._head = node._next
        self._size -= 1
        return answer

    def __str__(self):
        result = '['
        if self._size == 0:
            return '[]'
        else:
            node = self._head
            for i in range(self._size):
                if node == self._head:
                    result += str(node._element)
                    node = node._next
                else:
                    result += ', ' + str(node._element)
                    node = node._next
        result += ']'
        return result


if __name__ == '__main__':
    s = LinkedStack()
    assert len(s) == 0
    s.push(100)
    assert len(s) == 1
    assert s.top() == 100
    s.push(1000)
    assert len(s) == 2
    assert str(s) == "[1000, 100]"
    s.pop()
    assert str(s) == '[100]'
    s.pop()
    assert str(s) == '[]'