# DFS template
def dfs(root):
    # assume root is not None
    foo(root)
    root.visited = True
    for child in root.children:
        if not child.visited:
            dfs(child)


def foo(node):
    return node
