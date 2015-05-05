from _collections_abc import MutableMapping
from random import randrange

__author__ = 'inamoto21'


class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class"""

    #---------nested _Item class------------
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == self._value         # compare items based on keys

        def __ne__(self, other):
            return not self._key == self._value     # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key           # compare items based on their keys


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map"""
        self._table = []                # list of _Item's objects

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error: ' + repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present"""
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        # did not find match for key
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error: ' + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        """Generate iteration of map's keys"""
        for item in self._table:
            yield item._key                 # yield the key


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression"""
    def __init__(self, cap=11, p=109345121):
        """Create an empty hash table map"""
        self._table = cap * [None]
        self._n = 0                         # number of entries in the map
        self._prime = p                     # prime for MAD compression
        self._scale = 1 + randrange(p-1)    # scale from 1 to p-1 for MAD
        self._shift = randrange(p)          # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n              # number of items in the table

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)               # subroutine maintains self._n
        if self._n > len(self._table) // 2:         # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)  # number 2 * x - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, c):                           # resize bucket array to capacity c
        old = list(self.items())                    # use iteration to record existing items
        self._table = c * [None]                    # reset table to desired capacity
        self._n = 0                                 # n recomputed during subsequent adds
        for (k,v) in old:
            self[k] = v                             # reinsert old key-value pair


class ChainHashMap(HashMapBase):
    """Hash map implementing with separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()         # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:               # key was new to the table
            self._n += 1                                # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))       # no match found
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:                         # a non empty slot
                for key in bucket:
                    yield key

if __name__ == '__main__':
    s = ChainHashMap()
    s['A'] = 1              # key: A, value: 1
    s['B'] = 2              # key: B, value: 2
    s['C'] = 3
    s['AA'] = 11

    for i in s:             # print all the keys
        print(i)

    print(s['AA'])           # print the value of key: AA
    assert len(s) == 4
    del s['B']
    for i in s:             # print all the keys
        print(i)
    assert len(s) == 3