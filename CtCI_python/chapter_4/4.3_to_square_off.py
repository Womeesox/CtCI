from sys import path
from os import getcwd
path.append(getcwd())
from My_implementations.Graph import Graph
from My_implementations.Graph import Graph_node
from collections import deque

def list_of_depths(root_node):
    assert isinstance(root_node, Graph_node)
    
    list_of_deques = []
    parent_list = [root_node]

    while parent_list:
        for parent in parent_list:
            assert len(parent.children) <= 2
            new_deque = deque()
            new_parent_list = []

            for child in parent.children:
                new_deque.append(child)
                new_parent_list.append(child)

        parent_list = new_parent_list
        list_of_deques.append(new_deque)

    return list_of_deques

example = Graph()

root_node = example["a"]
root_node.add("b1").add("b2")
root_node.add("c1").add("c2")


print(list_of_depths(root_node))