# Write a program that compares the efficiency of insertion in start in linked list and array.

import array
import timeit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(pos-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.size += 1

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def insertInLinkedList(ll):
    timeStart = timeit.default_timer()
    for i in range(1, 10):
        ll.insert_at(i, 0)
    timeEnd = timeit.default_timer()
    print("Time taken: ", timeEnd - timeStart)


def insertInArray(arr):
    timeStart = timeit.default_timer()
    for i in range(1, 10):
        arr.insert(0, i)
    timeEnd = timeit.default_timer()
    print("Time taken: ", timeEnd - timeStart)


def main():
    ll = LinkedList()
    arr = array.array('i')
    insertInLinkedList(ll)
    print("Linked List:")
    ll.printList()
    print("========================")
    insertInArray(arr)
    print("Array:")
    print(arr)


main()
