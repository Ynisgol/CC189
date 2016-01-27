# This is topological sort.
from collections import deque


def topological_sort(nodes):
    # set inbounds for all the nodes
    for node in nodes:
        for neighbor in node.neighbors:
            neighbor.inbound += 1

    result = []
    # loop through all the nodes, put all nodes with 0 inbound into a queue
    # process the queue:
    # pop one item, add to the result and reduce the inbound of every neighbor of it by one. if the inbound
    # then reaches 0, add the neighbor to the queue
    # stop when the queue is empty
    # if the result.size < nodes.size, there is a cycle, and should return None
    q = deque()
    for node in nodes:
        if node.inbound == 0:
            q.append(node)
    while q:
        curr = q.popleft()
        result.append(curr)
        for neighbor in curr.neighbors:
            neighbor.inbound -= 1
            if neighbor.inbound == 0:
                q.append(neighbor)
    if len(result) < len(nodes):
        return None
    else:
        return result


class Graph:
    def __init__(self):
        self.nodes = set()


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.inbound = 0


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.neighbors.add(d)
f.neighbors.add(b)
b.neighbors.add(d)
f.neighbors.add(a)
d.neighbors.add(c)
res = topological_sort([a, b, c, d, e, f])
for nde in res:
    print nde.val,
