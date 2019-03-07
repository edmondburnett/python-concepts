#!/usr/bin/env python

from typing import List


class Node:
    """ Node class to represent each element in the linked list. """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """ Provides the interface to a linked list. """
    def __init__(self):
        self.head = Node()

    def append(self, data: int):
        # TODO allow adding of multiple new nodes at once
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        # TODO return the new node's position or address

    def length(self) -> int:
        current_node = self.head
        total_nodes = 0
        while current_node.next is not None:
            total_nodes += 1
            current_node = current_node.next
        return total_nodes

    def display(self) -> List:
        """ Display returns all elements in the structure """
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        return elements

    def get(self, index: int):
        # TODO use __getitem__ instead?
        if index >= self.length():
            raise IndexError("Linked List Index out of range.")
        current_index = 0
        current_node = self.head
        while True:
            # TODO don't use infinite loops even though we do error check above
            current_node = current_node.next
            if current_index == index:
                return current_node.data
            current_index += 1

    def remove(self, index):
        if index >= self.length():
            raise IndexError("Linked List Index out of range.")
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return 1
            current_index += 1



if __name__ == '__main__':
    ll = LinkedList()
    ll.append(13)
    ll.append(7)
    ll.append(24)
    ll.append(128)

    print("List of Linked List values: ", ll.display())
    print("Linked list length: ", ll.length())

    ll.remove(1)
    print("List of Linked List values after removing one: ", ll.display())
    print("Linked list length after removing one: ", ll.length())
