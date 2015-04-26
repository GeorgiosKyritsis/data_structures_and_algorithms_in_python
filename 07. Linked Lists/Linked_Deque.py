__author__ = 'inamoto21'

from Doubly_Linked_List import DoublyLinkedList


class LinkedDeque(DoublyLinkedList):

    def first(self):
        """Return but not remove the element at the front of the deque"""
        if self.is_empty():
            raise IndexError('Out of bounds')
        node = self.header.next
        return node.element

    def last(self):
        """Return but not remove the last element of the deque"""
        if self.is_empty():
            raise IndexError("Out of bounds")
        node = self.trailer.previous
        return node.element

    def insert_first(self, e):
        """Add an element to the front of the deque"""
        self.import_between(e, self.header, self.header.next)

    def insert_last(self, e):
        """Add an element to the back of the deque"""
        self.import_between(e, self.trailer.previous, self.trailer)

    def delete_first(self):
        """Remove and return the first element of the deque"""
        if self.is_empty():
            raise IndexError("Empty deque")
        return self.delete_node(self.header.next)

    def delete_last(self):
        """Remove and return the last element of the deque"""
        if self.is_empty():
            raise IndexError("Empty deque")
        return self.delete_node(self.trailer.previous)

    def __str__(self):
        result = '['
        node = self.header.next
        if node != None:
            result += str(node.element)
            node = node.next
            for i in range(self.size - 1):
                result += ", " + str(node.element)
                node = node.next
        result += ']'
        return result

if __name__ == '__main__':
    s = LinkedDeque()
    assert len(s) == 0
    s.insert_first(10)
    assert len(s) == 1
    assert str(s) == '[10]'
    s.insert_first(100)
    assert str(s) == '[100, 10]'
    assert s.first() == 100
    assert s.last() == 10
    s.delete_first()
    assert str(s) == '[10]'
    s.insert_first(1)
    print(s)