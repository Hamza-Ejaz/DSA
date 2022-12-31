# Write a program to check if the given string is palindrome using a deque.

class deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def printDeque(self):
        print(self.items)


def main():
    dq = deque()
    string = input("Enter a string: ")
    for i in string:
        dq.addRear(i)
    while dq.size() >= 2:
        frontItem = dq.removeFront()
        rearItem = dq.removeRear()
        if frontItem != rearItem:
            print("Not a palindrome")
            break
        else:
            print("Palindrome")
            break


main()
