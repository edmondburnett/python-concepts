#!/usr/bin/env python


class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if self.root is None:
            # if the root node is empty, just create a new node there
            self.root = Node(value)
        else:
            # call the private recursive _insert
            self._insert(value, self.root)

    def _insert(self, value: int, current_node):
        if value < current_node.value:
            # if the new value is less than the current node, insert it to the left
            if current_node.left_child is None:
                # if there's nothing at the left child, insert it there
                current_node.left_child = Node(value)
            else:
                # if there is something at the left child, set the current node
                # to left_child and call _insert again recursively
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            # value is greater than current_node's value, so move to the right
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)
        else:
            # value equals the current node value
            print("Value already exists in tree, skipping.")

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print(f"Current node's value: {current_node.value}")
            self._print_tree(current_node.right_child)

    def height(self) -> int:
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height: int) -> int:
        if current_node is None:
            return current_height
        left_height = self._height(current_node.left_child, current_height + 1)
        right_height = self._height(current_node.right_child, current_height + 1)
        return max(left_height, right_height)

    def search(self, value: int) -> bool:
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value: int, current_node) -> bool:
        if value == current_node.value:
            return True
        elif value < current_node.value and current_node.left_child is not None:
            return self._search(value, current_node.left_child)
        elif value > current_node.value and current_node.right_child is not None:
            return self._search(value, current_node.right_child)
        return False


def fill_tree(tree, num_elems: int = 100, max_int: int = 1000) -> BST:
    from random import randint
    for x in range(num_elems):
        current_elem = randint(0, max_int)
        tree.insert(current_elem)
    return tree


if __name__ == "__main__":
    tree = BST()
    #tree = fill_tree(tree)
    tree.insert(6)
    tree.insert(13)
    tree.insert(1)
    tree.insert(9)
    tree.insert(5)
    tree.insert(21)
    tree.insert(10)
    tree.insert(0)
    tree.insert(0)
    tree.print_tree()
    print(f"Tree height: {tree.height()}")
    print(tree.search(21))
    print(tree.search(33))
