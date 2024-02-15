from collections import deque

class Stack_with_min(deque):
    def __init__(self, iterable=None):
        super().__init__()
        self._min_stack = deque()

        if iterable:
            for item in iterable:
                self.append(item)


    def append(self, x):
        super().append(x)

        if not len(self._min_stack) == 0:
            if x < self._min_stack[-1][0]:
                self._min_stack.append([x, 1])
            else:
                self._min_stack[-1][1] += 1
        else:
            self._min_stack.append([x, 1])

    def pop(self):
        super().pop()

        if self._min_stack[-1][1] == 1:
            self._min_stack.pop()
        else:
            self._min_stack[-1][1] -= 1

    def __min__(self):
        try:
            return self._min_stack[-1]
        except IndexError:
            raise Exception("Deque is empty")
        
test_case = Stack_with_min([5, 3, 2, 1])

test_case.pop()
test_case.append(-10)
[test_case.pop() for _ in range(2)]
print(min(test_case))
print(test_case)