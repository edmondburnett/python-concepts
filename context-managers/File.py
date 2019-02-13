#!/usr/bin/env python


class file_manager:
    """ Define a context manager class for basic file i/o """

    def __init__(self, filename, open_as):
        self.file_object = open(filename, open_as)

    def __enter__(self):
        return self.file_object

    def __exit__(self, type, value, traceback):
        self.file_object.close()


if __name__ == '__main__':
    with file_manager('file.txt', 'a') as f:
        f.write('Hello! This line was written using a context manager class.\n')
