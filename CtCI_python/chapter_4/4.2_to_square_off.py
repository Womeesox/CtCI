from sys import path
from os import getcwd
path.append(getcwd())
from My_implementations.Graph import Graph
from My_implementations.Graph import Graph_node

def minimal_tree(list):
    parent_graph = Graph()

    root_node = parent_graph["a"]
    root_node.name = list[len(list) // 2]

    cravler_minimal_tree(list, root_node)
    def cravler_minimal_tree(sub_list, parent_node):
        middle_index = len(list) // 2

        if len(sub_list) > 1:
            left_child = cravler_minimal_tree(sub_list[:middle_index], sub_list[middle_index])
            right_child = cravler_minimal_tree(sub_list[middle_index:], sub_list[middle_index])
        else:
            


test_data = list(range(20))

example_graph = Graph()

root_node = example_graph["a"]

# def minimal_tree(list_for_tree):
#     assert isinstance(list_for_tree, list), "list_for tree has to be list type"
#     middle_node_index = len(list_for_tree) // 2
#     sub_lists = [list_for_tree[:middle_node_index], list_for_tree[middle_node_index:]]
    
#     return_graph = Graph()
#     root_node = return_graph["a"]
#     root_node.name = list_for_tree[middle_node_index]

#     while sub_lists:
#         new_sub_lists = []

#         for sub_list in sub_lists:
#             middle_node_index = len(sub_list) // 2
#             new_sub_lists.append(sub_list[:middle_node_index])
#             new_sub_lists.append(sub_list[middle_node_index:])
            

            

#         sub_lists = new_sub_lists

