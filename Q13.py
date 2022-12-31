# Write a program that input two queues of size 4, one with even numbers and other with odd numbers and merge them into a single queue.

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printQueue(self):
        print(self.items)

    def merge(self, q1, q2):
        if q1.isEmpty():
            print("Queue 1 is empty")
        if q2.isEmpty():
            print("Queue 2 is empty")
        while not q1.isEmpty() or not q2.isEmpty():
            if not q1.isEmpty():
                self.enqueue(q1.dequeue())
            if not q2.isEmpty():
                self.enqueue(q2.dequeue())
        self.printQueue()


a = Queue()
b = Queue()

a.enqueue(8)
a.enqueue(6)
a.enqueue(4)
a.enqueue(2)

b.enqueue(7)
b.enqueue(5)
b.enqueue(3)
b.enqueue(1)


q = Queue()
q.merge(a, b)
