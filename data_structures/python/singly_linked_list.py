#!/usr/bin/python3
"""
Implementing a singly linked list in Python
"""


class Node(object):
    """
    Setting up the class Node to allow for a singly linked list to have multiple elements
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.nextNode = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.nextNode

    def set_next(self, new_next):
        self.nextNode = new_next


class LinkedList(object):
    """
    Creating the Linked List class
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        """
        Method to insert a node into a linked list
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        """
        Method to get the size of a singly linked list
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current.get_next()
        return count

    def search(self, data):
        """
        Method to search for a given item in the list
        Returns the Node at which the data is found, otherwise raises an error
        """
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Data is not in the list")
        return current

    def delete(self, data):
        """
        Method to delete a given node
        Raises a ValueError if the data cannot be found
        """
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")

        if previous is None:
            self.head = current.get_next()
        else:
            previous.setNext(current.get_next())
