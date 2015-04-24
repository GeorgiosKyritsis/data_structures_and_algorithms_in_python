__author__ = 'inamoto21'


class LinkedList():
    """A linked list using a list as the underlying storage"""

    class Node():           # Nested class
        """A Node of a singly linked list"""

        def __init__(self, k):      # A Node with value k and no next
            self.key = k
            self.next = None

    def __init__(self):
        """A new empty linked list"""
        self.head = None
        self.num_elements = 0

    def index(self, v):     # Return the index of the element with value v
        i = 0
        node = self.head
        while node and node.key != v:
            node = node.next
            i += 1
        if node:
            return i
        else:
            return ValueError("{} is not in the linked list".format(v))

    def insert(self, i, v):
        if i < 0 or i > self.num_elements:
            raise IndexError("insert index out of range")
        new_node = LinkedList.Node(v)
        if i == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            for j in range(i-1):
                node = node.next
            new_node.next = node.next
            node.next = new_node
        self.num_elements += 1

    def append(self, v):
        self.insert(self.num_elements, v)

    def pop(self, i):       # Remove element at index i
        if i < 0 or i > self.num_elements:
            raise IndexError("pop index out of bounds")
        if i == 0:
            node = self.head
            result = node.key
            self.head = node.next
        else:
            node = self.head
            for j in range(i-1):
                node = node.next
            result = node.next.key
            node.next = node.next.next
        self.num_elements -= 1
        return result

    def __len__(self):
        return self.num_elements

    def __str__(self):
        result = '['
        node = self.head
        if node != None:
            result += str(node.key)
            node = node.next
            for i in range(self.num_elements - 1):
                result += ", " + str(node.key)
                node = node.next
        result += ']'
        return result

if __name__ == "__main__":
        s = LinkedList()
        assert len(s) == 0
        assert str(s) == '[]'
        s.append(100)
        assert len(s) == 1
        assert str(s) == '[100]'
        s.append(1000)
        assert len(s) == 2
        assert str(s) == '[100, 1000]'
        assert s.index(1000) == 1
        s.pop(0)
        assert str(s) == '[1000]'
        assert s.pop(0) == 1000
        assert len(s) == 0
        assert str(s) == '[]'