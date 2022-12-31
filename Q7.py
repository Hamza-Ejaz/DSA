# Write a program to create an unordered singly linked list with 10 elements.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
            print(last)
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


linkedList = LinkedList()

linkedList.append(11)
linkedList.append(7)
linkedList.append(-9)
linkedList.append(8)
linkedList.append(2)
linkedList.append(-6)
linkedList.append(0)

linkedList.printList()
