from sys import path
from os import getcwd
path.append(getcwd())
from My_implementations.Graph import Graph
from My_implementations.Graph import Graph_node
from collections import deque

def is_there_route(node1: Graph_node, node2: Graph_node) -> bool:
    parent_graph = node1.parent_graph_instance

    queue = deque()
    processed = set()
    queue.append(node1.name)

    while queue:     
        curr_processing = queue[-1]  
        del queue[-1]

        if node2.name == curr_processing:
            return True
        processed.add(curr_processing)
        
        for child in parent_graph[curr_processing].children:
            if child.name not in processed:
                queue.append(child.name)
                processed.add(child.name)

    return False

example_graph = Graph()

example_graph["a"].add("b").add("c")
example_graph["a"].add("a1").add("a2")
example_graph["a1"].add("a11")

node_d = Graph_node("d", example_graph, [example_graph["c"]])

# print(example_graph["a1"].children) 

print(is_there_route(example_graph["a"], example_graph["a11"]))


