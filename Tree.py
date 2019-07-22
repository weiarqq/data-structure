class Binary_Node():
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None


def define_tree():
    root = Binary_Node(5)
    root.left = Binary_Node(4)
    root.right = Binary_Node(3)
    root.right.left = Binary_Node(2)


class Node():
    def __init__(self, val):
        self.key = val
        self.children = []


def def_tree():
    root = Node(5)
    root.children.append(Node(4))