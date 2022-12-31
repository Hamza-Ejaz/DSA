# Write a program to add/multiply two numbers using stack

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def multiply(self):
        a = self.pop()
        b = self.pop()
        self.push(a*b)

    def add(self):
        a = self.pop()
        b = self.pop()
        self.push(a+b)


stack = Stack()  # create an object of class Stack
stack.push(2)   # push 2 to the stack
stack.push(6)   # push 6 to the stack
stack.multiply()    # multiply the two numbers
print(stack.pop())  # pop and print the result

stack.clear()   # clear the stack

stack.push(21)  # push 21 to the stack
stack.push(5)  # push 5 to the stack
stack.add()  # add the two numbers
print(stack.pop())  # pop and print the result
