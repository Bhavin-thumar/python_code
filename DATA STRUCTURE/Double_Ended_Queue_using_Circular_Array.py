class  Empty(Exception):
    pass

class DequeArray:

    DEFAULT_CAPACITY = 5

    def __init__(self):
        self.arr = [None] * DequeArray.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0
        self.rear = 0


    def __len__(self):
        return self.size


    def resize(self, cap):

        old = self.arr
        start = self.front
        self.arr = [None] * cap

        for i in range(self.size):
            self.arr[i] = old[start]
            start = (start + 1) % self.size

        self.front = 0
        self.rear = self.size - 1


    def is_empty(self):
        return self.size == 0


    def is_full(self):
        return self.size == len(self.arr)


    def get_front(self):
        return self.front

    def get_rear(self):
        return self.rear


    def display(self):
        start = self.front
        while start != self.rear:
            print(self.arr[start], end = '<---')
            start = (start + 1) % len(self.arr)

        print(self.arr[self.rear])
        print()


    def insert_rear(self, n):
        if self.is_empty():

            self.arr[self.rear] = n
            self.size += 1

        else:
            if self.is_full():
                self.resize(2*len(self.arr))

            self.rear = (self.rear + 1) % len(self.arr)
            self.arr[self.rear] = n
            self.size += 1


    def insert_front(self, n):
        if self.is_empty():

            self.arr[self.front] = n
            self.size += 1

        else:
            if self.is_full():
                self.resize(2 * len(self.arr))
            #     self.front = len(self.arr) - 1
            # elif self.front != 0:
            #     self.front -= 1
            # else:
            #     self.front = len(self.arr) - 1
            self.front = (self.front - 1) % len(self.arr)
            self.arr[self.front] = n
            self.size += 1

        # elif not self.is_full() and self.front != 0:
        #     self.front -= 1
        #     self.arr[self.front] = n
        #     self.size += 1

        # elif self.front == 0:
        #     self.front = len(self.arr) - 1
        #     self.arr[self.front] = n
        #     self.size += 1

        # elif self.is_full():
        #     self.resize(2*len(self.arr))
        #     self.front = len(self.arr) - 1
        #     self.arr[self.front] = n
        #     self.size += 1


    def delete_front(self):
        if self.is_empty():
            raise Empty("Queue is Empty")

        elif self.size != 1:
            answer = self.arr[self.front]
            self.arr[self.front] = None
            self.front = (self.front + 1) % len(self.arr)
            self.size -= 1

        else:
            answer = self.arr[self.front]
            self.arr[self.front] = None
            self.size -= 1
            self.front = 0
            self.rear = 0

        if self.size == 0:
            self.front = 0
            self.rear = 0

        return answer


    def delete_rear(self):
        if self.is_empty():
            raise Empty("Queue is Empty")

        else:
            answer = self.arr[self.rear]
            self.arr[self.rear] = None
            self.rear = (self.rear - 1) % len(self.arr)
            self.size -= 1


        # elif self.rear != 0:
        #     answer = self.arr[self.rear]
        #     self.arr[self.rear] = None
        #     self.rear -= 1
        #     self.size -= 1

        # elif self.rear == 0:
        #     answer = self.arr[self.rear]
        #     self.arr[self.rear] = None
        #     self.rear = len(self.arr) - 1
        #     self.size -= 1

        if self.size == 0:
            self.front = 0
            self.rear = 0

        return answer

D = DequeArray()
D.insert_front(10)
D.insert_rear(20)
D.insert_front(30)
D.insert_rear(40)
D.insert_front(50)
D.insert_rear(60)
D.insert_front(70)
D.insert_rear(80)
D.insert_front(90)
D.insert_rear(100)
D.display()
D.delete_front()
D.delete_rear()
D.display()
D.delete_front()
D.delete_rear()
D.display()
D.delete_front()
D.delete_rear()
D.display()
D.delete_front()
D.delete_rear()
D.display()
D.delete_front()
D.delete_rear()
D.display()
print(D.size)
print(D.get_front())
print(D.get_rear())









