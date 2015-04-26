__author__ = 'inamoto21'


class Doubly_Linked_List:
    """Implementation of a Doubly linked list with sentinels (header, trailer)"""

    class Node:
        def __init__(self, element, previous, next):
            self.element = element
            self.previous = previous
            self.next = next

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer             # trailer is after header
        self.trailer.previous = self.header         # header is before trailer
        self.size = 0                               # size of the list

    def __len__(self):
        """Return the length of the list"""
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        """Return but not remove the first element of the List"""
        if self.is_empty():
            raise IndexError("Empty list")
        node = self.header.next
        return node.element

    def last(self):
        """Return but not remove the last element of the list"""
        if self.is_empty():
            raise IndexError("Empty list")
        node = self.trailer.previous
        return node.element

    def push(self, e):
        """Add an element the end of the list"""
        new_node = self.Node(e, self.trailer.previous, self.trailer)
        self.trailer.previous.next = new_node
        self.trailer.previous = new_node
        self.size += 1

    def pop(self):
        """Remove the last element of the list"""
        if self.is_empty():
            raise IndexError("Empty list")
        removed_node = self.trailer.previous
        removed_node.previous.next = self.trailer
        self.trailer.previous = removed_node.previous
        self.size -= 1

    def add_first(self, e):
        """Add an element at the beginning of the list"""
        new_node = self.Node(e, self.header, self.header.next)
        self.header.next.previous = new_node
        self.header.next = new_node
        self.size += 1

    def delete_first(self):
        """Remove the first element of the list"""
        removed_node = self.header.next
        removed_node.next.previous = self.header
        self.header.next = removed_node.next
        self.size -= 1

    def index(self, e):
        """Return the index of the element with value e"""
        i = 0
        node = self.header.next
        while node and node.element != e:
            node = node.next
            i += 1
        if node:
            return i
        else:
            return ValueError("{} is not in the list".format(e))

    def insert(self, i, e):
        """Insert element e at index i"""
        if i < 0 or i > self.size:
            raise IndexError("The index is out of range")
        new_node = self.Node(e, None, None)
        if i == 0:
            new_node.previous = self.header
            new_node.next = self.header.next
            self.header.next.previous = new_node
            self.header.next = new_node
        else:
            node = self.header.next
            for j in range(i-1):
                node = node.next
            new_node.next = node.next
            new_node.previous = node
            node.next.previous = new_node
            node.next = new_node
            self.size += 1

    def __str__(self):
        """Return the string representation of class Doubly_Linked_List instance"""
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

    def __iter__(self):
        node = self.header.next
        for j in range(self.size):
            yield node.element
            node = node.next

if __name__ == '__main__':
    s = Doubly_Linked_List()
    s.push(1)
    s.push(2)
    s.push(3)
    s.add_first(10)
    s.push(100)
    assert str(s) == '[10, 1, 2, 3, 100]'
    s.insert(1, 200)
    assert str(s) == '[10, 200, 1, 2, 3, 100]'
    s.insert(3, 555)
    assert str(s) == '[10, 200, 1, 555, 2, 3, 100]'
    s.delete_first()
    assert str(s) == '[200, 1, 555, 2, 3, 100]'
    s.pop()
    assert str(s) == '[200, 1, 555, 2, 3]'
    assert len(s) == 5
    # Check the iterator
    for i in s:
        print(i)        # Types all the elements of the list