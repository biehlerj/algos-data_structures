#!/usr/bin/python3
'''
Implementing a singly linked list in Python
'''

class Node(object):
    '''
    Setting up the class Node to allow for a singly linked list to have multiple elements
    '''
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.nextNode

    def setNext(self, newNext):
        self.nextNode = newNext

class LinkedList(object):
    '''
    Creating the Linked List class
    '''
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        '''
        Method to insert a node into a linked list
        '''
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        '''
        Method to get the size of a singly linked list
        '''
        current = self.head
        count = 0
        while current:
            count += 1
            current.getNext()
        return count
    
    def search(self, data):
        '''
        Method to search for a given item in the list
        Returns the Node at which the data is found, otherwise raises an error
        '''
        current = self.head
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        
        if current is None:
            raise ValueError("Data is not in the list")
        return current

    def delete(self, data):
        '''
        Method to delete a given node
        Raises a ValueError if the data cannot be found
        '''
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if current is None:
            raise ValueError("Data not in list")
        
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
