from collections import deque


# BFS template
def bfs(root):
    q = deque()
    root.marked = True
    q.append(root)
    while q:
        node = q.popleft()
        foo(node)  # do something on node
        for child in node.children:
            if not child.marked:
                child.marked = True
                q.append(child)


def foo(node):
    return node
