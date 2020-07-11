class Empty(Exception):
    pass


class ArrayQueue:

    DEFAULT_CAPACITY = 5

    def __init__(self):
        self.arr = [None] * ArrayQueue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        self.rear = 0


    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0


    def resize(self, cap):
        old = self.arr
        self.arr = [None] * cap
        start = self.front
        for i in range(self.size):
            self.arr[i] = old[start]
            start = (start + 1) % len(old)

        self.front = 0
        self.rear = len(old) - 1


    def enqueue(self, data):
        if self.is_empty():
            self.arr[self.rear] = data
            self.size += 1

        else:
            if self.size == len(self.arr):
                self.resize(2 * len(self.arr))
            self.rear = (self.rear + 1) % len(self.arr)
            self.arr[self.rear] = data
            self.size += 1


    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is Empty")
        elif self.size == 1:
            dequeue_data = self.arr[self.front]
            self.arr[self.front] = None
            self.front = 0
            self.rear = 0
            self.size -= 1
        else:
            dequeue_data = self.arr[self.front]
            self.arr[self.front] = None
            self.front = (self.front + 1) % len(self.arr)
            self.size -= 1

        return dequeue_data


    def first(self):
        return self.arr[self.front]


    def display(self):
        start = self.front
        end = self.rear
        while start != end:
            print(self.arr[start], end = '<---')
            start = (start + 1) % len(self.arr)
        print(self.arr[end], end = '<---')
        print()




cqu = ArrayQueue()
cqu.enqueue(11)
cqu.enqueue(22)
cqu.enqueue(33)
cqu.enqueue(44)
cqu.enqueue(55)
cqu.dequeue()
cqu.dequeue()
cqu.dequeue()
cqu.enqueue(66)
cqu.enqueue(77)
print(cqu.size)
cqu.enqueue(88)
cqu.display()
print(cqu.arr)
print(cqu.first())
print(f'front index is : {cqu.front}')
print(f'rear index is : {cqu.rear}')
