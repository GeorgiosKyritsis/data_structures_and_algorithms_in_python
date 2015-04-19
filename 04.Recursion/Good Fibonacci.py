__author__ = 'inamoto21'


import  unittest


def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a,b) = good_fibonacci(n-1)
        return (a+b,a)


class TestFib(unittest.TestCase):
    def test_1(self):
        self.assertEqual(good_fibonacci(5), (5,3))

    def test_2(self):
        self.assertEqual(good_fibonacci(7), (13,8))

    def test_3(self):
        self.assertEqual(good_fibonacci(12), (144,89))


def main():
    print(good_fibonacci(5))


if __name__ == '__main__':
    main()
