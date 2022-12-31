# Write a program that implements a simple phone book directory using a doubly linked list.

class Node:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insertAt(self, index, name, number):
        if index >= self.count:
            print("Index out of range")
            return
        newNode = Node(name, number)
        if index == 0:
            self.insertAtStart(name, number)
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            newNode.next = temp.next
            newNode.prev = temp
            temp.next.prev = newNode
            temp.next = newNode
            self.count += 1

    def insertAtStart(self, name, number):
        newNode = Node(name, number)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.count += 1
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.count += 1

    def printList(self):
        temp = self.head
        while temp:
            print(temp.name + " - ", temp.number)
            temp = temp.next


def main():
    dll = DoublyLinkedList()
    dll.insertAtStart('E', '555-1234')
    dll.insertAtStart('D', '444-1234')
    dll.insertAtStart('C', '333-1234')
    dll.insertAtStart('B', '222-1234')
    dll.insertAtStart('A', '111-1234')
    # dll.insertAt(0, 'A', '1')
    # dll.insertAt(1, 'B', '2')
    # dll.insertAt(2, 'C', '3')
    # dll.insertAt(3, 'D', '4')
    # dll.insertAt(4, 'E', '5')
    # dll.insertAt(5, 'F', '6')
    dll.printList()


main()
