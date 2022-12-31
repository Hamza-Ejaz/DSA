# Write a program to copy all the items from a queue to stack.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    # def size(self):
    #     return len(self.items)

    # def length(self):
    #     return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        self.items = []

    def clone(self):
        return self.items.copy()


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


stack = Stack()
queue = Queue()

stack.push(2)
stack.push(7)
stack.push(18)
stack.push(-6)

copyOfStack = stack.clone()


def copyToQueue(stackClone, queue):
    for i in range(len(stackClone)):
        queue.enqueue(stackClone.pop())


copyToQueue(copyOfStack, queue)

queue.printQueue()
