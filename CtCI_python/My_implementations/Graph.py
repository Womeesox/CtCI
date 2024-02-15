class Graph():
    def __init__(self):
        self.nodes = dict()
        self.nodes["a"] = Graph_node("a", self)

    def __getitem__(self, key):
        return self.nodes[key]

class Graph_node():
    def __init__(self, name, parent_graph_instance, children=None):
        if children is not None:
            assert isinstance(children, list)
        else:
            children=[]
        assert isinstance(parent_graph_instance, Graph)
        
        if name in parent_graph_instance.nodes:
            raise Exception("node with that name already exsists")

        self.name = name
        self.children = children

        parent_graph_instance.nodes[name] = self
        self.parent_graph_instance = parent_graph_instance

    def add(self, name):
        if name in self.parent_graph_instance.nodes:
            raise Exception("node with that name already exsists")

        new_node = Graph_node(name, self.parent_graph_instance)
        self.children.append(new_node)
        self.parent_graph_instance.nodes[name] = new_node

        return new_node

    def __repr__(self):
        return f"{self.name}"