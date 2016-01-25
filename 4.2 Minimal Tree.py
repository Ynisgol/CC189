def minimal_bst(array):
    # do it recursively
    # returns the root of the BST built
    # say n = len(array), array[n / 2] will be the root, and built left and right
    return minimal_bst_helper(array, 0, len(array) - 1)


# need a helper that accepts start index and end index
def minimal_bst_helper(array, start, end):
    if start > end:
        return None
    if start == end:
        return Node(array[start])
    mid = (start + end + 1) / 2
    root = Node(array[mid])
    root.left = minimal_bst_helper(array, start, mid - 1)
    root.right = minimal_bst_helper(array, mid + 1, end)
    return root


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def in_order_traverse(root):
    if root:
        in_order_traverse(root.left)
        print str(root.val) + " ",
        in_order_traverse(root.right)


in_order_traverse(minimal_bst([1, 2, 3, 4, 5, 6]))
