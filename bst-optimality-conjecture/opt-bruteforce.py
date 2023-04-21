import sys


class Request:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class BSTNode:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def rotate(self):
        if self.parent is None:
            return

        if self.parent.parent is not None:
            if self.parent.parent.left == self.parent:
                self.parent.parent.left = self
            else:
                self.parent.parent.right = self

        if self.parent.left == self:
            self.parent.left = self.right
            if self.right is not None:
                self.right.parent = self.parent
            self.right = self.parent
        else:
            self.parent.right = self.left
            if self.left is not None:
                self.left.parent = self.parent
            self.left = self.parent

        self.parent.parent = self
        self.parent = self.parent.parent.parent


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return

        node = self.root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = BSTNode(value, parent=node)
                    node = node.left
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = BSTNode(value, parent=node)
                    node = node.right
                    break
                node = node.right

        while node.parent is not None:
            node.rotate()

        self.root = node

    def delete(self, value):
        if self.root is None:
            return

        node = self.root
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                break

        if node is None:
            return

        while node.parent is not None:
            node.rotate()

        self.root = node

        if self.root.left is None:
            self.root = self.root.right
            if self.root is not None:
                self.root.parent = None
        else:
            node = self.root.left
            while node.right is not None:
                node = node.right
            node.right = self.root.right
            if node.right is not None:
                node.right.parent = node


def offline_optimal(sigma):
    pass


def main():
    bst = BST()
    n = int(input())
    for _ in range(n):
        request = input().split()
        if request[0] == '+':
            bst.insert(int(request[1]))
        elif request[0] == '-':
            bst.delete(int(request[1]))
        else:
            print('YES' if bst.root is not None and bst.root.value ==
                  int(request[1]) else 'NO')
