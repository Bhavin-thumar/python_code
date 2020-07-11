
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node


    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return
        else:
            temp = self.front
            self.front = self.front.next
            print("Deque :", temp.data)
            temp = None
            if self.front is None:
                self.rear = None



    def is_empty(self):
        return self.front is None

    def display(self):
        instance = self.front
        while instance is not None:
            print(instance.data, end = '--->')
            instance = instance.next

        print()


Myqueue = Queue()

Myqueue.enqueue(11)
Myqueue.enqueue(22)
Myqueue.enqueue(33)
Myqueue.enqueue(44)

Myqueue.display()
Myqueue.dequeue()
Myqueue.display()
Myqueue.dequeue()
print(Myqueue.is_empty())
Myqueue.dequeue()
Myqueue.dequeue()
print(Myqueue.is_empty())
print(Myqueue.rear)
print(Myqueue.front)
Myqueue.display()
