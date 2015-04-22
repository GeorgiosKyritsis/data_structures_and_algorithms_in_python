__author__ = 'inamoto21'

import unittest


def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)


def main():
    print(bad_fibonacci(10))



class testFib(unittest.TestCase):

    def test_1(self):
        self.assertEqual(bad_fibonacci(3), 2)

    def test_2(self):
        self.assertEqual(bad_fibonacci(6), 8)

    def test_3(self):
        self.assertEqual(bad_fibonacci(12), 144)



if __name__ == '__main__':
    main()