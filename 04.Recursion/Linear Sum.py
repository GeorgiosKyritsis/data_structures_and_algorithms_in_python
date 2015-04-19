__author__ = 'inamoto21'


def linear_sum(S, n):
    """
    :param S: a sequence
    :param n: the first n numbers of the sequence
    :return: The sum of the first n numbers of the sequence
    """

    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]


def main():
    seq = [1, 2, 3, 4, 5]
    total = linear_sum(seq, 3)
    print(total)


if __name__ == '__main__':
    main()

