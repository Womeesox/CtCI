from sys import path
from os import getcwd
path.append(getcwd())
from My_implementations.Linked_list_node import Linked_list_node


"""two problems
1. not working for two digit sum at the end
2. not working for different lengths of lists"""
def sum_lists_reverse(list1_head, list2_head):
    return_head = Linked_list_node()

    return_node = return_head
    list1_node = list1_head
    list2_node = list2_head
    passed_to_next = 0

    while list1_node or list2_node:
        assert isinstance(list1_node.data, int) and isinstance(list2_node.data, int) and list1_node.data >= 0 and list2_node.data >= 0, "every node of both lists have to be positive ints"

        list_sum = list1_node.data + list2_node.data
        if passed_to_next == 1:
            list_sum += 1
            passed_to_next = 0

        if list_sum > 9:
            return_node.data = list_sum - 10
            passed_to_next = 1
        else:
            return_node.data = list_sum
        
        list1_node = list1_node.next
        list2_node = list2_node.next

        if list1_node or list2_node:
            return_node.next = Linked_list_node()
            return_node = return_node.next


    return return_head
        #992 + 21 = 1013
        #2 -> 9 -> 9  +  1 -> 2  =  3 -> 1 -> 0 -> 1

test_case = [Linked_list_node.create_linked_list((2, 9, 1)), Linked_list_node.create_linked_list((3, 3, 2))]

print(sum_lists_reverse(test_case[0], test_case[1]).print_linked_list())