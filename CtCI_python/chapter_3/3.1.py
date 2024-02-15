from typing import Literal, Any

class Stack3_list_implementation():
    def __init__(self, iterable1=None, iterable2=None, iterable3=None, stack_importance=None):
        self._stack_list = []

    def append(self, stack_nr: Literal[1, 2, 3], item) -> None:
        self._stack_list.append([stack_nr, item])

    def peek(self, stack_nr: Literal[1, 2, 3]):
        for pair in reversed(self._stack_list):
            if pair[0] == stack_nr:
                return pair[1]
    
    def pop(self, stack_nr: Literal[1, 2, 3]):
        for count, pair in enumerate(reversed(self._stack_list)):
            if pair[0] == stack_nr:
                del self._stack_list[len(self._stack_list) - 1 - count]
                break
    
example = Stack3_list_implementation()

example.append(1, 2)
example.append(1, 3)

example.pop(1)
example.pop(1)
example.pop(1)
example.append(1,"A")

example.pop(2)
print (f"peek3: {example.peek(1)}")
print(f"peek2: {example.peek(2)}")