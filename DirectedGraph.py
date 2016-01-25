from Node import Node


class DirectedGraph:
    def __init__(self):
        self.nodes = set()
        self.node_dict = {}

    def initialize(self, dictionary):
        for key, value in dictionary.iteritems():
            self.add_by_key(key)
            self.add_by_key(* value)
            for v in value:
                self[key].add_children(self[v])

    def __contains__(self, key):
        return key in self.node_dict

    def __getitem__(self, * keys):
        if len(keys) == 1:
            return self.node_dict[keys[0]]
        else:
            return [self[key] for key in keys]

    def get(self, key):
        if key in self:
            return self.node_dict[key]
        else:
            return None

    def add(self, * nodes):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.add(node)
                self.node_dict[node.val] = node
                for child in node.children:
                    self.add(child)

    def add_by_key(self, * keys):
        for key in keys:
            if key not in self:
                n = Node(key)
                self.add(n)

    def __iter__(self):
        return iter(self.nodes)

    def __str__(self):
        s = ""
        for node in self:
            s += str(node) + "\n"
        return s

dg = DirectedGraph()
dg.add_by_key(1, 2, 3)
dg.initialize({1: [2, 3],
               2: [3],
               3: [2],
               4: [3, 5]})
print dg

