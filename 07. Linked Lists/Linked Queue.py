__author__ = 'inamoto21'


class LinkedQueue:
    """FIFO Queue implementation of a singly linked list as storage"""
    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next


    def __init__(self):
        """Create an empty queue"""
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        """Return but not remove the first element of the Queue"""
        if self.is_empty():
            raise IndexError('Index out of bounds')
        node = self.head
        return node.element

    def dequeue(self):
        """Return and remove the first element of the queue"""
        if self.is_empty():
            raise IndexError('Index out of bounds')
        node = self.head
        answer = node.element
        self.head = node.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return answer

    def enqueue(self, v):
        """Push an element into the end of the Queue"""
        new_node = self.Node(v, None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def __str__(self):
        result = '['
        if self.size == 0:
            return '[]'
        else:
            node = self.head
            for i in range(self.size):
                if node == self.head:
                    result += str(node.element)
                    node = node.next
                else:
                    result += ', ' + str(node.element)
                    node = node.next
        result += ']'
        return result

if __name__ == '__main__':
    s = LinkedQueue()
    s.enqueue(10)
    s.enqueue(100)
    print(s)
    s.dequeue()
    print(s)
    s.dequeue()
    print(s)

