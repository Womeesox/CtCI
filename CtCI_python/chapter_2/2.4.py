import unittest, random
from sys import path
from os import getcwd
path.append(getcwd())
from My_implementations.Linked_list_node import Linked_list_node

def partition_to_pivot(head_node, pivot):
    assert isinstance(head_node, Linked_list_node), "head_node has to be instance of Linked_list_node"
    current_node = head_node

    while current_node:
        assert isinstance(current_node.data, int), "all nodes in linked list have to be ints"
        print(Linked_list_node.print_linked_list(head_node))

        next_node = current_node.next #it's needed cuz current_node.next can change

        if current_node.data < pivot:
            if "last_node_smaller_than_pivot" in locals():
                previous_node.next = current_node.next
                current_node.next = last_node_smaller_than_pivot.next
                last_node_smaller_than_pivot.next = current_node
            elif "previous_node" in locals():
                if current_node.next:
                    previous_node.next = current_node.next
                current_node.next = head_node
                head_node = current_node

            last_node_smaller_than_pivot = current_node

        previous_node = current_node
        current_node = next_node
    
    return head_node

test_case = list(range(10))
random.shuffle(test_case)

test_case = Linked_list_node.create_linked_list(tuple(test_case))

print(Linked_list_node.print_linked_list(partition_to_pivot(test_case, 5)))