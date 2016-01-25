class Node:
    def __init__(self, value):
        self.val = value
        self.children = []
        self.marked = False
        self.visited = False
        self.marked1 = False
        self.marked2 = False

    def add_children(self, * children):
        for child in children:
            self.children.append(child)

    def initialize(self, value, * children_values):
        self.val = value
        self.children += [Node(v) for v in children_values]
        return self

    def __str__(self):
        s = str(self.val) + ": "
        for child in self.children:
            s += str(child.val) + ", "
        if s[-2:] == ", ":
            return s[:-2]
        else:
            return s


# print Node(None).initialize(5, 4, 3, 1, 2, 3)
