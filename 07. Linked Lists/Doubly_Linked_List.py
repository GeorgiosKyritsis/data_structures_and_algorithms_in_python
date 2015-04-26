__author__ = 'inamoto21'


class DoublyLinkedList:
    """Implementation of a Doubly linked list with sentinels (header, trailer)"""
    class Node:
        def __init__(self, element, previous, next):
            self.element = element
            self.previous = previous
            self.next = next

    def __init__(self):
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer                     # trailer is after header
        self.trailer.previous = self.header                 # header is before trailer
        self.size = 0                                       # number of elements

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def import_between(self, v, predecessor, successor):
        """Add element between to existing nodes and return new node"""
        new_node = self.Node(v, predecessor, successor)
        predecessor.next = new_node
        successor.previous = new_node
        self.size += 1
        return new_node

    def delete_node(self, node):
        """Delete a node from the list and return its element"""
        predecessor = node.previous
        successor = node.next
        predecessor.next = successor
        successor.previous = predecessor
        self.size -= 1
        element = node.element
        node.previous = node.next = node.element = None
        return element