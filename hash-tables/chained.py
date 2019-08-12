#!/usr/bin/env python

""" Implementing hash table data structure using a chaining / linked-list
means of resolving collisions.
"""


class Node:
    def __init__(self, key: str, value: int):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.containers = [None] * self.capacity

    def hash(self, key: str):
        sum = 0
        for index, char in enumerate(key):
            #sum = sum + (index + len(key)) ** ord(char)
            sum += (index + ord(char))
        return sum % self.capacity

    def insert(self, key: str, value: int):
        self.length += 1
        index = self.hash(key)
        node = self.containers[index]
        if not node:
            self.containers[index] = Node(key, value)
            return True
        else:
            previous_node = node
            while node is not None:
                previous_node = node
                node = node.next
            previous_node.next = Node(key, value)
            return True
        # TODO: handle case where a duplicate node already exists - overwrite

    def find(self):
        pass

    def remove(self):
        pass


if __name__ == "__main__":
    ht = HashTable(64)
    hash = ht.hash("Microsoft")
    ht.insert("Microsoft", 87)
    print(ht.containers[hash].key, ht.containers[hash].value)
