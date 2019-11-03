#!/usr/bin/python3
"""
Implementing a doubly linked list in Python
"""


class Node(object):
    """
    Defining the nodes of the list
    """

    def __init__(self, data, prev, next_node):
        self.data = data
        self.prev = prev
        self.next_node = next_node


class LinkedList(object):
    """
    Defining the functions available for a doubly linked list
    """
    head = None
    tail = None

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next_node = None
            self.tail.next_node = new_node
            self.tail = new_node

    def delete(self, node_value):
        current = self.head
        found = False

        while current is not None and found is False:
            if current.data == node_value:
                if current.prev is not None:
                    if current != self.tail:
                        current.prev.next_node = current.nextNode
                        current.next_node.prev = current.prev
                    else:
                        current.prev.next_node = None
                    found = True
                else:
                    self.head = current.next_node
                    current.next_node.prev = None
                    found = True

            current = current.next_node

        if current is None and found is False:
            raise ValueError("Value not in list")

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next_node

        return count

    def search(self, node_value):
        current = self.head
        found = False

        while current is not None and found is False:
            if current.data == node_value:
                found = True
            else:
                current = current.next_node

        if current is None:
            raise ValueError("Value is not in the list")

        return current
