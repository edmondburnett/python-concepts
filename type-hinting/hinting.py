#!/usr/bin/env python

from typing import List


def expand_list(mylist: List) -> str:
    for item in mylist:
        print(item)
    return "Hello world"


if __name__ == '__main__':
    expand_list([1, 2, 3])
