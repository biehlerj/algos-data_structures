#!/usr/bin/python3
'''
Implementing a doubly linked list in Python
'''

class Node(object):
    '''
    Defining the nodes of the list
    '''
    def __init__(self, data, prev, nextNode):
        self.data = data
        self.prev = prev
        self.nextNode = nextNode

class LinkedList(object):
    '''
    Defining the functions available for a doubly linked list
    '''
    head = None
    tail = None

    def append(self, data):
        newNode = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.prev = self.tail
            newNode.nextNode = None
            self.tail.nextNode = newNode
            self.tail = newNode

    def delete(self, nodeValue):
        current = self.head
        found = False

        while current is not None and found is False:
            if current.data == nodeValue:
                if current.prev is not None:
                    if current != self.tail:
                        current.prev.nextNode = current.nextNode
                        current.nextNode.prev = current.prev
                    else:
                        current.prev.nextNode = None
                    found = True
                else:
                    self.head = current.nextNode
                    current.nextNode.prev = None
                    found = True
            
            current = current.nextNode
        
        if current is None and found is False:
            raise ValueError("Value not in list")
    
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.nextNode
        
        return count

    def search(self, nodeValue):
        current = self.head
        found = False
        
        while current is not None and found is False:
            if current.data == nodeValue:
                found = True
            else:
                current = current.nextNode
            
        if current is None:
            raise ValueError("Value is not in the list")
        
        return current
