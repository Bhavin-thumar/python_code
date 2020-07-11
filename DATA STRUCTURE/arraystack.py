from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.container.pop()

    def peek(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.container[-1]

    def __len__(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0

    def __repr__(self):
        return f'{self.container}'


def is_matched(expr):
    op = '({['
    close = ')}]'
    s = Stack()
    for c in expr:
        if c in op:
            s.push(c)
        elif c in close:
            if s.is_empty():
                return False
            if close.index(c) != op.index(s.pop()):
                return False
    return S.is_empty()

print(is_matched('({[])}'))
