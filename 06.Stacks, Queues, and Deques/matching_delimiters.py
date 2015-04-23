__author__ = 'inamoto21'

import Stack


def is_matched(expr):
    """Return True if delimiters are properly matched. False otherwise"""
    lefty = "({["
    righty = ")}]"

    s = Stack.ArrayStack()
    for c in expr:
        if c in lefty:
            s.push(c)
        elif c in righty:
            if s.is_empty():
                return False
            if righty.index(c) != lefty.index(s.pop()):
                return False
    return s.is_empty()


def main():
    expr = "[[({})]]"
    print(is_matched(expr))

    expr = '(({})]'
    print(is_matched(expr))


if __name__ == '__main__':
    main()