# Write a program that takes a sequence of round braces from user and checks if the parenthesis is balanced or not.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def length(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def peak(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def clear(self):
        self.items = []

    def printStack(self):
        print(self.items)

    def bracketCheck(self, string):
        for i in string:
            self.push(i)

        count = 0

        for i in range(self.size()):
            if self.peak() == '(':
                self.pop()
                count += 1
            elif self.peak() == ')':
                self.pop()
                count -= 1

        if count == 0:
            print("Balanced")
        else:
            print("Not Balanced")


stack = Stack()
stack.bracketCheck("(())")
