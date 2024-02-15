import sys
from typing import Tuple, Any

class Linked_list_node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data
    
    @staticmethod
    def create_linked_list(nodes: Tuple[Any]):
        head_node = Linked_list_node(None)
        node = head_node
        for element in nodes[:-1]:
            node.next = Linked_list_node(None)
            node.data = element
            node = node.next
        node.data = nodes[-1]
        return head_node

    def print_linked_list(self): 
        output_string = ""
        node = self
        while node is not None:
            if node.next is not None: 
                output_string = output_string + f"{node.data} -> "
            else:
                 output_sting = output_string + str(node.data)
            node = node.next
        
        return output_sting

