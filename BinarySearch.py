__author__ = 'inamoto21'

import unittest


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2  # floor of the middle
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)


class TestBinary(unittest.TestCase):

    def test_1(self):
        self.assertEqual(binary_search(range(3), 1, 0, 2), True)

    def test_2(self):
        self.assertEqual(binary_search(range(25), 23, 0, 24), True)

    def test_3(self):
        self.assertEqual(binary_search(range(25), 26, 0, 24), False)

def main():
    x = range(25)
    result = binary_search(x, 2, 0, 24)
    print(result)



if __name__ == '__main__':
    main()