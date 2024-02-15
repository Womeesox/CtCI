#write code to remove duplicates from unsorted linked list
import unittest
from sys import path
from os import getcwd
path.append(getcwd())
from My_implementations.Linked_list_node import Linked_list_node

def remove_duplicates(starting_node):
    assert isinstance(starting_node, Linked_list_node), "Node must be Linked_list"
    buffer_table = set()

    node = starting_node
    prev = None
    while node is not None:
        if node.data in buffer_table:
            prev.next = node.next
        else:
            buffer_table.add(node.data)
        
        prev = node
        node = node.next
    
    return starting_node

#I know it's not working. Solution is trivial
def remove_duplicates_nobuffer(starting_node):
    node = starting_node
    node_counter = 0
    runner_counter = 0
    prev = None

    while node is not None:
        runner = starting_node
        while runner is not None:
            if not runner_counter == node_counter and runner.data == node.data:
                prev.next = node.next
            runner = runner.next
            runner_counter += 1

        prev = node
        node = node.next
        node_counter += 1
    
    return starting_node
     

class Test(unittest.TestCase):
    functions_to_test = [remove_duplicates]

    test_cases = {
        Linked_list_node.create_linked_list(("a", "b", "b", "c", "a")): "a -> b -> c",
        Linked_list_node.create_linked_list((2, "d", True, 2, False, True)): "2 -> d -> True -> False",
        Linked_list_node.create_linked_list((1, 1, 1, 1)): "1 -> 1"
    }
    
    def test_check_permutation(self):
        for function in self.functions_to_test:
            for arg, expected in self.test_cases.items():
                result = function(arg).print_linked_list()
                assert result == expected, f"For: {function.__name__} expected: {expected} and instead got: {result}"

if __name__ == "__main__":
        unittest.main()
