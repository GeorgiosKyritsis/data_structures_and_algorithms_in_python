__author__ = 'inamoto21'

class CircularQueue:
    """Queue implementation using a circular linked list"""
    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        """Return but not remove the first element of the Queue"""
        if self.is_empty():
            return IndexError('Index out of bounds')
        node = self.tail.next
        return node.element

    def dequeue(self):
        """Return and remove the first element of the Queue"""
        if self.is_empty():
            raise IndexError('Index out of bounds')
        node = self.tail.next
        answer = node.element
        if self.size == 1:
            self.tail = None
        else:
            self.tail.next = node.next
        self.size -= 1
        return answer

    def enqueue(self, v):
        """Add an element to the queue"""
        new_node = self.Node(v, None)
        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def __str__(self):
        result = '['
        if self.is_empty():
            return '[]'
        else:
            node = self.tail.next
            for i in range(self.size):
                if node == self.tail.next:
                    result += str(node.element)
                    node = node.next
                else:
                    result += ', ' + str(node.element)
                    node = node.next
        result += ']'
        return result

if __name__ == '__main__':
    s = CircularQueue()
    print(s)
    s.enqueue(10)
    s.enqueue(100)
    s.enqueue(1000)
    assert len(s) == 3
    print(s)
    assert s.first() == 10
    s.dequeue()
    assert str(s) == '[100, 1000]'
    print(s)
    s.dequeue()
    s.dequeue()
    print(s)
    s.dequeue()     #Raises an IndexError