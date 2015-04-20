__author__ = 'inamoto21'


def binary_sum(S, start, stop):

    """
    :param S: sequence
    :param start: start
    :param stop: end
    :return: the sum of the slice of the sequence
    """

    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


def main():
    seq = range(3, 10, 3)
    print(binary_sum(seq, 0, len(seq)))


if __name__ == '__main__':
    main()