# Use a stack to evaluate the postfix expression 1 2 + 3 4 * - 9 /. Write the state of the stack after each token (i.e., an operator or operand) is processed.

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        self.items = []

    def clone(self):
        return self.items.copy()

    def printStack(self):
        print(self.items)


def postfix(exp):
    stack = Stack()
    for i in exp:
        if i.isdigit():
            stack.push(int(i))
        else:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.push(a + b)
                print(str(a) + " + " + str(b) + " = " + str(a + b))
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.push(-a + b)
                print(str(a) + " - " + str(b) + " = " + str(-a + b))
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.push(a * b)
                print(str(a) + " * " + str(b) + " = " + str(a * b))
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                stack.push(a / b)
                print(str(a) + " / " + str(b) + " = " + str(a / b))
    return stack.pop()


print(postfix('1 2 + 3 4 * - 9 /'))
