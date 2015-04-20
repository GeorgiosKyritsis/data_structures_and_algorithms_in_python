__author__ = 'inamoto21'

import unittest


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(binary_search_iterative(range(10), 10), False)

    def test_2(self):
        self.assertEqual(binary_search_iterative(range(10), 9), True)


def binary_search_iterative(data, target):
    """

    :param data: sequence
    :param target: the element to find
    :return: True if found, otherwise False
    """

    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def main():
    seq = range(3,10,3)
    print(binary_search_iterative(seq, 6))

if __name__ == '__main__':
    main()