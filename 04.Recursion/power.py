__author__ = 'inamoto21'


def power(x, n): # A trivial way O(n)
    """
    :param x: base
    :param n: exponent
    :return: result of the calculation
    """

    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

def power1(x, n): # A sophisticated way

    if n == 0:
        return 1
    else:
        partial = power1(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


def main():
    c = power(2, 4)
    print(c)

    c1 = power1(2, 4)
    print(c1)


if __name__ == '__main__':
    main()
