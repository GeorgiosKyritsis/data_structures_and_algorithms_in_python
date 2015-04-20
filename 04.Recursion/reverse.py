__author__ = 'inamoto21'

import unittest

def reverse(S, start, stop):
    """
    :param S: sequence of elements
    :param start: start of the sequence
    :param stop: end of the sequence
    :return: reverse elements of the slice
    """

    if start < stop - 1:  # if at least 2 elements
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse(S, start+1, stop-1)
    return S


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse([1, 2, 3, 4], 0, 4), [4, 3, 2, 1])

    def test_2(self):
        self.assertEqual(reverse(['a', 'b', 'c', 'd'], 0, 4), ['d', 'c', 'b', 'a'])

def main():
    seq = [1, 2, 3, 4, 5, 6, 7]
    rev_seq = reverse(seq, 0, len(seq))
    print(rev_seq)



if __name__ == '__main__':
    main()
