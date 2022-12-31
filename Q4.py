# Write a program to reverse a string using stack

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

    def pop(self):
        return self.items.pop()

    def clear(self):
        self.items = []

    # the reverse function is just a smart way of doing it!

    # def reverse(self, string):
    #     for i in range(len(string)):
    #         self.push(string[i])
    #     return self.items[::-1]

    # if you're into the more advanced stuff, you can these two functions inplace of the reverse function above

    def stringPush(self, string):
        for i in string:
            self.push(i)

    def stringPop(self, string):
        reveresedString = ''
        for i in string:
            reveresedString = reveresedString + self.pop()
        print(reveresedString)


stack = Stack()

stack.stringPush("Hello")
stack.stringPop("Hello")
