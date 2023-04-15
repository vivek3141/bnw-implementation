from collections import defaultdict


class BSTNode:
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def rotate(self):
        if self.parent is None:
            return

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

        tmp = self.parent.parent
        self.parent.parent = self
        self.parent = tmp

    def __str__(self):
        return str(self.value)


class SplayTree:
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
            self.root = self.root.left
            self.root.parent = None

    def find(self, value):
        if self.root is None:
            return None

        node = self.root
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                while node.parent is not None:
                    node.rotate()

                self.root = node
                return node

        return None

    def __str__(self):
        if self.root is None:
            return ""
        
        queue = [self.root]
        levels = defaultdict(list)
        curr_level = 1
        max_level = self.get_height(self.root)

        while curr_level <= max_level:
            num_nodes = len(queue)
            for _ in range(num_nodes):
                node = queue.pop(0)
                if node:
                    levels[curr_level].append(str(node))
                else:
                    levels[curr_level].append("")

                if node:
                    queue += [node.left, node.right]
                else:
                    queue += [None, None]
            curr_level += 1

        result = ""
        s = 2 ** (max_level - 1)
        for i in sorted(levels.keys()):
            for j in range(len(levels[i])):
                if j == 0:
                    result += " " * (s - (len(levels[i][j]) // 2)) + levels[i][j]
                else:
                    result += " " * (s - (len(levels[i][j]) // 2) - (len(levels[i][j-1]) // 2)) + levels[i][j]
            result += "\n"
            s //= 2

        return result[:-1]

    def get_height(self, node):
        if node is None:
            return 0
        else:
            left = self.get_height(node.left)
            right = self.get_height(node.right)
            return 1 + max(left, right)


def main():
    tree = SplayTree()
    tree.insert(52)
    tree.insert(316)
    tree.insert(7151)
    tree.insert(1141)
    tree.insert(415252)
    tree.insert(6131)
    tree.insert(8123123)
 
    print(tree)
    # tree.delete(3)
    # print(tree)
    # tree.delete(5)
    # print(tree)
    # tree.delete(1)
    # print(tree)
    # tree.delete(8)
    # print(tree)
    # tree.delete(4)
    # print(tree)
    # tree.delete(6)
    # print(tree)
    # tree.delete(7)
    # print(tree)


if __name__ == "__main__":
    main()
