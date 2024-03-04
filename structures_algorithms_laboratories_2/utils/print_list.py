import sys


def print_list(list, file = sys.stdout):
    for e in list:
        print(e, file=file)