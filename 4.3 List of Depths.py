from collections import deque


def list_of_depths(root):
    lists = []

    if root:
        q = deque()
        q.append(root)
        while q:
            head = Node(0)  # dummy head
            tail = head
            for _ in range(len(q)):
                tail.next = q.popleft()
                tail = tail.next
                if tail.left:
                    q.append(tail.left)
                if tail.right:
                    q.append(tail.right)
            lists.append(head.next)

    return lists


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.left = None
        self.right = None


rt = Node(0)
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
rt.left = a
rt.right = b
a.left = c
b.right = d
d.left = e

lists = list_of_depths(rt)
for head in lists:
    while head:
        print head.val,
        head = head.next
    print

