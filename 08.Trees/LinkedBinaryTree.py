__author__ = 'inamoto21'


class Tree:
    """Abstract Base class representing a Tree Structure"""

    #-------------------nested Position Class------------------------
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """Return the element stored in this position."""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other Position does not represent the same location"""

    #---------Abstract methods that concrete subclass must support-------------
    def root(self):
        """Return the Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children that position p has"""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):
        """Return the total numbers of elements in the tree"""
        raise NotImplementedError("must be implemented by subclass")

    #------Concrete methods implemented in this Class---------------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if position p does not have any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0


class BinaryTree(Tree):
    """Abstract Base class representing a binary tree structure"""

    #--------------additional abstract methods-------------------
    def left(self, p):
        """Return a Position representing p's left child, return None if p does not have a left child"""
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a Position representing p's right child, return None if p does not have a right child"""
        raise NotImplementedError("must be implemented by subclass")

    #------------concrete methods implemented in this class--------
    def sibling(self, p):
        """Return a position representing p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if parent is None:      # p must be the tree's root
            return None         # p has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)       # possibly None
            else:
                return self.right(parent)       # possibly None

    def children(self, p):
        """"Generate an iteration of Positions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    class _Node:
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An Abstraction representing the location of a single element."""
        def __init__(self, container, node):
            """Constuctor should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this position"""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:          #convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    #---------------binary tree constructor------------
    def __init__(self):
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0

    #---------------public accessors-----------------
    def __len__(self):
        """Return the total number of elements"""
        return self._size

    def root(self):
        """Return the root position of the tree or None if tree is empty."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the position of p's left child (or None if no left child)"""
        node = self._validate(p)
        return  self._make_position(node._left)

    def right(self, p):
        """Return the position of p's right child (or None if no right child)"""
        node = self._validate(p)
        return  self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:      # left child exists
            count += 1
        if node._right is not None:     # right child exists
            count += 1
        return count

    def _add_root(self, e):
        """Place element at the root of the empty tree and return the position of the root"""
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e

        Return the Position of new node.
        Raise ValueError if position p is invalid or p already has a left child"""

        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists")
        self._size += 1
        node._left = self._Node(e, node)            # node is parent
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e

        Return the Position of new node.
        Raise ValueError if position p is invalid or p already has a right child"""

        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)           # node is parent
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element of position p with e and return old element"""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that has been stored at position p.
        Raise ValueError if Position p is invalid or p has two children"""

        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        child = node._left if node._left else node._right       # might be None
        if child is not None:
            child._parent = node._parent                        # child's grandparent becomes child's parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node                                     # deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p"""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("position is not a leaf")
        if not type(self) is type(t1) is type(t2):      # all 3 types must be the same type
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():                           # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None                             # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    def __iter__(self):
        """Generate an iteration on the tree's elements"""
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def positions(self):
        """Generate an iteration of tree's position"""
        return self.preorder()


    # ----------------user interface for binary search tree----------------
    def add_element(self, e, p=-1):
        if self.is_empty():
            p = self._add_root(e)
            p = self.root()
        else:
            if p == -1:
                p = self.root()
            if e < p.element():
                if self.left(p) is None:
                    self._add_left(p, e)
                else:
                    self.add_element(e, self.left(p))
            else:
                if self.right(p) is None:
                    self._add_right(p, e)
                else:
                    self.add_element(e, self.right(p))

if __name__ == '__main__':
    s = LinkedBinaryTree()
    s.add_element(10)
    s.add_element(15)
    s.add_element(16)
    s.add_element(1)
    s.add_element(4)
    s.add_element(5)
    s.add_element(2)
    assert len(s) == 7

    for e in s:
        print(e)