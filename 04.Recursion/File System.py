__author__ = 'inamoto21'

import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print('{0:<7}'.format(total), path)
    return total


def main():
    path = '/home/inamoto21/Downloads/Python Cookbook 3rd Edition 2013'
    a = disk_usage(path)
    print(a)


if __name__ == '__main__':
    main()