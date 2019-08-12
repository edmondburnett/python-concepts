#!/usr/bin/env python


def bubblesort(l):
    changes = True
    pass_num = len(l) - 1
    while pass_num > 0 and changes:
        changes = False
        for index in range(pass_num):
            if l[index] > l[index + 1]:
                changes = True
                tmp = l[index]
                l[index] = l[index + 1]
                l[index + 1] = tmp
        pass_num = pass_num - 1
    return l


if __name__ == '__main__':
    print(bubblesort([7, 3, 10, 6, 4, 8, 5, 7]))
