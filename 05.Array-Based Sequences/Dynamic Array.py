__author__ = 'inamoto21'

import ctypes  # import low-level arrays
from time import time


class DynamicArray:
    """A dynamic array akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array"""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)          # low-level array

    def _make_array(self, c):           # non-public utility
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __setitem__(self, k, v):            # k intentionally left unused
        if self._n == self._capacity:       # not enough room
            self._resize(2 * self._capacity)        # double the size of the Array
        self._A[self._n] = v
        self._n += 1

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid Index')
        return self._A[k]           # retrieve from array

    def append(self, obj):
        """Add object to end of the array
        """
        if self._n == self._capacity:       # not enough room
            self._resize(2 * self._capacity)        # double the size of the Array
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._make_array(c)         # new bigger array
        for k in range(self._n):        # for each existing array
            B[k] = self._A[k]
        self._A = B         # use the bigger array
        self._capacity = c

    def insert(self, k, value):
        """Insert value at index k.
        For simplicity 0<=k<=n
        """
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurence of value
        else raise ValueError
        """
        for k in range(self._n):
            if self._A[k] == value:                 # found a match
                for j in range(k, self._n - 1):         # shift others to fill gap
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None        # help garbage collection
                self._n -= 1            # we have one less item
                return          # exit immediately
        raise ValueError('value not found')


def compute_average(n):
    """Perform n appends to empty list and return the average time"""
    data = []
    start = time()
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start) / n


def main():
    dynamic_array = DynamicArray()          # create an empty dynamic array

    for k in range(1000):       # 1000 appends to the empty dynamic array
        dynamic_array[k] = k        # dynamic_array.append(k)

    for i in range(1000):
        print(dynamic_array[i])

    dynamic_array[1000] = 2
    print(dynamic_array[1000])

    print(compute_average(1000))

    dynamic_array.insert(2, 100)            # insert at index 2 the value 100

    print('\n----------------\n')

    dynamic_array.remove(10)            # remove the first 10 of the dynamic array

    for i in range(len(dynamic_array)):
        print(dynamic_array[i])

if __name__ == '__main__':
    main()
