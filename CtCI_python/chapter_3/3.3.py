from collections import deque

class Set_of_stacks():
    def __init__(self, max_stack=5):
        self.max_stack = max_stack
        self._list_of_stacks = [deque()]

    def append(self, item):
        if len(self._list_of_stacks[-1]) > self.max_stack - 1:
            self._list_of_stacks.append(deque())
            self._list_of_stacks[-1].append(item)
        else:
            print(len(self._list_of_stacks[-1]), item)
            self._list_of_stacks[-1].append(item)

    def pop(self):
        if len(self._list_of_stacks[-1]) == 1:
            del self._list_of_stacks[-1]
        else:
            self._list_of_stacks[-1].pop()

    def popAt(self, i):
        if len(self._list_of_stacks[i]) == 1:
            del self.list_of_stacks[i]
        else:
            self._list_of_stacks[i].pop()

    def peek(self):
        return self._list_of_stacks[-1][-1]


    

    
