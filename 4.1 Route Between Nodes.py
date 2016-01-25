from collections import deque
from Node import Node


# BFS
def bfs(node1, node2):
    # assume neither node1 nor node2 is None
    q = deque()
    node1.marked = True
    q.append(node1)
    while q:
        n = q.popleft()
        if n == node2:
            return True
        for child in n.children:
            if not child.marked:
                child.marked = True
                q.append(child)
    return False


# DFS
def dfs(node1, node2):
    if node1 == node2:
        return True
    node1.visited = True
    for child in node1.children:
        if not child.visited and dfs(child, node2):
            return True
    return False


# bidirectional search, not applicable for directed graph
def bds(node1, node2):
    # assume neither node1 nor node2 is None
    q1 = deque()
    q2 = deque()
    s1 = set()
    s2 = set()

    node1.marked = True
    s1.add(node1)
    q1.append(node1)
    node2.marked = True
    s2.add(node2)
    q2.append(node2)

    while q1 and q2:
        n1 = q1.popleft()
        if n1 in s2:
            return True
        for child in n1.children:
            if not child.marked1:
                child.marked1 = True
                s1.add(child)
                q1.append(child)
        n2 = q2.popleft()
        if n2 in s1:
            return True
        for child in n2.children:
            if not child.marked2:
                child.marked2 = True
                s2.add(child)
                q2.append(child)

    return False

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n2.children = [n3, n4]
n3.children = [n2]
n4.children = [n2]

print bds(n2, n4)
