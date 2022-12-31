# Write a program to empty all items from stack to queue.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    # def length(self):
    #     return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        self.items = []


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


def stackToQueue(stack, queue):
    for i in range(stack.size()):
        queue.enqueue(stack.pop())


stack = Stack()
queue = Queue()

stack.push(2)
stack.push(6)
stack.push(13)
stack.push(10)
stack.push(7)

stackToQueue(stack, queue)

queue.printQueue()
