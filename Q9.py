# Write a program that inserts an element in a circular linked list at the center

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def getLength(self):
        return self.count

    def insertAtStart(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.count += 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.count += 1

    def insertAtCenter(self, index, data):
        if index >= self.count:
            print("Index out of range")
            return
        newNode = Node(data)
        if index == 0:
            self.insertAtStart(data)
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            newNode.next = temp.next
            newNode.prev = temp
            temp.next.prev = newNode
            temp.next = newNode
            self.count += 1

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def insertInLinkedList():
    for i in range(1, 6):
        data = int(input("Enter the data: "))
        cll.insertAtStart(data)


cll = circularLinkedList()
insertInLinkedList()
print("The list is: ")
cll.printList()
print("============================")
centerData = int(input("Enter the data to be inserted at center: "))
cll.insertAtCenter(int(cll.getLength() / 2), centerData)
print("============================")
print("The list is: ")
cll.printList()
