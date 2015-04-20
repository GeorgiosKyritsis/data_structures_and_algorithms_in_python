__author__ = 'inamoto21'


def reverse_iterative(S):
    """

    :param S: sequence
    :return: return reversed sequence
    """
    start = 0
    stop = len(S)
    while start < stop-1:
        temp = S[start]
        S[start] = S[stop-1]
        S[stop-1] = temp
        start += 1
        stop -= 1
    return S


def main():
    seq = [1, 2, 3, 4, 5, 6]
    print(reverse_iterative(seq))


if __name__ == '__main__':
    main()