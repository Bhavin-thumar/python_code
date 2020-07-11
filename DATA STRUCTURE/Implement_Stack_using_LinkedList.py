class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Stack:
    def __init__(self):
        self.top = None


    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node


    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return
        else:
            next = self.top.next
            current = self.top
            print(current.data)
            self.top = next
            del current


    def peek(self):
        return self.top.data

    def is_empty(self):
        return self.top is None


    def display(self):
        instance = self.top
        while instance is not None:
            print(instance.data, end = '--->')
            instance = instance.next
        print()


MyStack = Stack()

MyStack.pop()
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)

MyStack.display()

print('Top element is :', MyStack.peek())

MyStack.pop()
MyStack.pop()

MyStack.display()

print('Top element is :', MyStack.peek())

MyStack.pop()
MyStack.pop()

print(MyStack.is_empty())
